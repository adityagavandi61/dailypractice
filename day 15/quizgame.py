import random
class PythonQuiz:
    def __init__(self):
        self.questions = {
            "What is Python?": {
                "options": ["A. A snake", "B. A programming language", "C. A database", "D. A web browser"],
                "correct": "B"
            },
            "What are Python’s key features?": {
                "options": ["A. Static typing", "B. Manual memory management", "C. Dynamic typing and extensive libraries", "D. No built-in data structures"],
                "correct": "C"
            },
            "How do you define a function in Python?": {
                "options": ["A. function myFunc()", "B. define myFunc()", "C. def myFunc():", "D. func myFunc()"],
                "correct": "C"
            },
            "What is the difference between a list and a tuple?": {
                "options": ["A. Lists are immutable, tuples are mutable", "B. Lists are mutable, tuples are immutable", "C. Both are mutable", "D. Both are immutable"],
                "correct": "B"
            },
            "What is a dictionary in Python?": {
                "options": ["A. A collection of key-value pairs", "B. A list of words", "C. An ordered collection of values", "D. A data structure that stores only keys"],
                "correct": "A"
            },
            "How do you create a dictionary in Python?": {
                "options": ["A. Using ()", "B. Using {}", "C. Using []", "D. Using <>"],
                "correct": "B"
            },
            "How do you access values in a dictionary?": {
                "options": ["A. Using keys", "B. Using indexes", "C. Using .get()", "D. Both A and C"],
                "correct": "D"
            },
            "How do you add a new key-value pair to a dictionary?": {
                "options": ["A. dict.append(key, value)", "B. dict[key] = value", "C. dict.add(key, value)", "D. dict.insert(key, value)"],
                "correct": "B"
            },
            "How do you remove a key from a dictionary?": {
                "options": ["A. del dict[key]", "B. dict.remove(key)", "C. dict.pop(key)", "D. Both A and C"],
                "correct": "D"
            },
            "How do you iterate over a dictionary?": {
                "options": ["A. Using dict.forEach()", "B. Using for key in dict:", "C. Using for key, value in dict.items():", "D. Both B and C"],
                "correct": "D"
            }
        }

    def display_questions(self):
        score = 0
        keys = list(self.questions.keys())
        random.shuffle(keys)
        for question in keys:
            options = self.questions[question]
            print(f"Q: {question}")
            for option in options["options"]:
                print(option)
            answer = input("Enter a correct option: ").upper()
            score += 1 if answer == options['correct'] else 0
            result = "Correct!\n" if answer == options['correct'] else "Oops, you are wrong!\n"
            print(result)
        wrong_answer = len(self.questions) - score
        print(f"Your total is {score}.")

# Example usage
quiz = PythonQuiz()
quiz.display_questions()
