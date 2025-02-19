import random
from questions import generate_quiz
import json
import pyttsx3

class PythonQuiz:
    # text to speak
    def Speak_text(self,command): 
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    def fetch_json(self):
        self.Speak_text("Enter your name")
        creater = input("Enter your name: ")
        self.Speak_text("Enter your topic name")
        topic = input("Enter a topic for quiz (eg.Python Programing and for exit type 'bye'): ")
        if topic == 'bye':
            print("Good bye!")
            break
        else:
            self.Speak_text("Enter a number of question to be generated")
            numbers_of_questions = int(input('Enter a number of question to be generated: (min 5): '))
            if numbers_of_questions < 5:
                print('Enter 5 and above.')
                self.Speak_text("Oops! Enter 5 and above.")
            else:
                print(f"Generating a quiz on: {topic}")
                print(f"Number of questions: {numbers_of_questions}")
                print("Quiz generating....")
                self.Speak_text("Wait for a few seconds.")
                generated_quiz = generate_quiz(creater, topic, numbers_of_questions)
                with open(generated_quiz, 'r') as jsonfile:
                    data = json.load(jsonfile)
                return data

    def display_questions(self):
        data = self.fetch_json()
        try:
            score = 0
            topic = data['topic']
            self.Speak_text(f"Quiz is successfully generated on {topic}.")
            print('\n\t', topic, '\t\n')
            for quiz_data in data['questions']:
                question = quiz_data['Question text']
                print(f"Q: {question}")
                self.Speak_text(f"Your question is {question}")
                self.Speak_text("Your options are")
                for option in quiz_data['options']:
                    print(option)
                    self.Speak_text(option)
                answer = input("Enter a correct option: ").strip().upper()
                score += 1 if answer == quiz_data['correct_answer'] else 0
                result = "Correct!\n" if answer == quiz_data['correct_answer'] else "Oops, you are wrong!\n"
                if result == "Oops, you are wrong!\n":
                    self.Speak_text(result)
                    print(result)
                    self.Speak_text(f"and correct and is {quiz_data['correct_answer']}.")
                    print(f"and correct and is {quiz_data['correct_answer'][0]}.")
                else:
                    self.Speak_text(result)
                    print(result)

            print(f"Your total is {score}/{len(data['questions'])}.")
            self.Speak_text(f"Your total is {score} out of {len(data['questions'])}.")
        except Exception as e:
            print("")


# Example usage
quiz = PythonQuiz()
quiz.display_questions()
