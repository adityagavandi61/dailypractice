from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2")

chain = prompt | model

while True:
    question = input("You: ")
    if question.strip() == "":
        print("AI Chat: Please ask a question.")
        continue
    if question.strip().lower() == "bye":
        print("AI Chat: Goodbye!")
        break
    response = chain.invoke({"question": question})
    print("AI Chat:", response)
