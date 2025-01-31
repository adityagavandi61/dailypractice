import google.generativeai as genai

api_key = 'your_api_key'

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
inp = input("Enter a prompt... ")
response = model.generate_content(inp)
print(response.text)