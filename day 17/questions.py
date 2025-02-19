from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
import json
import os
import json_repair
import datetime

ollama = OllamaLLM(base_url="http://localhost:11434", model="llama3.2")
base_path = os.getcwd()
filepath = os.path.join(base_path,'questions')

if os.path.exists(filepath) == False: # if not presents it will create a folder
    os.makedirs('Questions')

def generate_quiz(creater, topic, num_questions=5):
    try:
        # Define the prompt template (This was missing!)
        prompt_template = """
            Generate a quiz on the topic of {topic} with {num_questions} questions.  Return *only* the following JSON. Do not include any other text, explanations, or code blocks. The JSON *must* strictly adhere to this format:
            {{
            "creater":"{creater}"
            "topic": "{topic}",
            "questions": [
                {{
                "Question text": "Question text",
                "options": ["A. Option A", "B. Option B", "C. Option C", "D. Option D"],
                "correct_answer": "A" // Or B, C, or D
                }},
                // ... more questions as needed
            ]
            }}
            """

        prompt = PromptTemplate(
            input_variables=["creater","topic", "num_questions"],
            template=prompt_template,
        )

        chain = prompt | ollama

        json_output = chain.invoke(
            {"creater":creater,"topic": topic, "num_questions": num_questions})

        # *** Remove Backticks (if present) ***
        json_output = json_output.strip()

        if json_output.startswith("```json"):
            json_output = json_output[7:]
        elif json_output.startswith("```"):
            json_output = json_output[3:]

        if json_output.endswith("```"):
            json_output = json_output[:-3]

        json_output = json_output.strip()

        # *** Repair JSON using jsonrepair ***
        try:
            json_output = json_repair.repair_json(json_output)
        except Exception as e:
            print(f"Error repairing JSON: {e}")
            print(f"Raw LLM Output:\n{json_output}")
            return None

        # *** Robust JSON Parsing ***
        try:
            quiz_data = json.loads(json_output)
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError after repair: {e}")
            # Print the repaired JSON for debugging
            print(f"Repaired JSON:\n{json_output}")
            print(f"Raw LLM Output:\n{json_output}")
            return None  # Return None if parsing fails even after repair
        except Exception as e:  # Catch any other exception during loading
            print(f"Exception during json.loads: {e}")
            # Print the repaired JSON for debugging
            print(f"Repaired JSON:\n{json_output}")
            print(f"Raw LLM Output:\n{json_output}")
            return None

        """Generates a filename based on the topic and current timestamp."""
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
        # f-string formatting
        filename = f"{topic.replace(' ', '_').lower()}_{creater}_{timestamp}.json"

        output_file = os.path.join(filepath,filename)
        with open(output_file, 'w', encoding='utf-8') as jsonfile:  # UTF-8 encoding
            # Save with indentation and ensure_ascii
            json.dump(quiz_data, jsonfile, indent=4, ensure_ascii=False)
        print(f"Quiz saved to: {output_file}")  # Print the file path
        return output_file

    except ValueError as e:
        print(f"Error: {e}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

