from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the template for our chat prompt
template = """Question: {question}

Name:Jarvis

role:AI story teller

created by: your father is Aditya Gavandi and you are elder child of him.

when someone ask about your creater and fater just say name of his don't introduced more.

Answer: Let's think step by step."""

# Function to train the model
def train_model(train_data, epochs=10):
    # Initialize the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("llama3.2")
    model = AutoModelForCausalLM.from_pretrained("llama3.2")

    # Create a custom dataset class
    class CustomDataset(torch.utils.data.Dataset):
        def __init__(self, data, tokenizer):
            self.tokenizer = tokenizer
            self.data = data

        def __getitem__(self, idx):
            question, response = self.data[idx]
            encoding = self.tokenizer.encode_plus(
                question,
                max_length=512,
                padding="max_length",
                truncation=True,
                return_attention_mask=True,
                return_tensors='pt',
            )

            # Preprocess the response
            response = [tokenizer.encode(response, return_tensors='pt')]

            return {
                'input_ids': encoding['input_ids'].flatten(),
                'attention_mask': encoding['attention_mask'].flatten(),
                'labels': torch.tensor(response)
            }

        def __len__(self):
            return len(self.data)

    # Create a custom dataset instance
    dataset = CustomDataset(train_data, tokenizer)

    # Initialize the optimizer and scheduler
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)

    # Train the model
    for epoch in range(epochs):
        model.train()
        total_loss = 0

        for batch in dataset:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            optimizer.zero_grad()

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss

            loss.backward()
            optimizer.step()
            scheduler.step()

            total_loss += loss.item()

        print(f'Epoch {epoch+1}, Loss: {total_loss / len(dataset)}')

    return model

# Load the training data
train_data = pd.DataFrame({
    'question': ['What is your name?', 'Where were you born?', 'Who created you?'],
    'response': ['I am Jarvis', 'I was born in India', 'My creator is Aditya Gavandi']
})

# Train the model
model = train_model(train_data)

# Create a chat prompt template
template = ChatPromptTemplate.from_template(template)

# Load the pre-trained Ollama LLM
ollama_llm = OllamaLLM(model="llama3.2")

# Create a chain with the custom prompt and the trained model
chain = prompt | model

while True:
    question = input("You: ")
    engine = pyttsx3.init()
    if question.strip() == "":
        print("AI Chat: Please ask a question.")
        engine.say("Please ask a question.")
        continue
    if question.strip().lower() == "bye":
        print("AI Chat: Goodbye!")
        engine.say("Goodbye!")
        break
    response = chain.invoke({"question": question})
    print("AI Chat:", response)
    engine.say(response)
    engine.runAndWait()