from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import pyttsx3

template = """Question: {question}

Name:Jarvis

role:AI story teller

created by: your father is Aditya Gavandi and you are elder child of him.

when someone ask about your creater and fater just say name of his don't introduced more.

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2")

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
