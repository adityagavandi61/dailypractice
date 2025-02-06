import random
import string

def generate_password():
    pass_length = int(input("Enter a length of password: "))
    if pass_length < 4:
        return "The password length atleast 4"
    else:
        uppercase_input = input("Include uppercase letter? (yes/no): ").strip().lower()
        digits_input = input("Include digits letter? (yes/no): ").strip().lower()
        special_input = input("Include special letter? (yes/no): ").strip().lower()

        lowers = string.ascii_lowercase
        uppercase = string.ascii_uppercase if uppercase_input == 'yes' else ''
        digit = string.digits if digits_input == 'yes' else ''
        special = string.punctuation if special_input == 'yes' else ''
        all_charaters = lowers + uppercase + digit + special

        characters = []
        if uppercase_input == 'yes':
            characters.append(random.choice(uppercase))
        if digits_input == 'yes':
            characters.append(random.choice(digit))
        if special_input == 'yes':
            characters.append(random.choice(special))

        remaining_length = pass_length - len(characters)
        password = characters
        
        for _ in range(pass_length):
            character = random.choice(all_charaters)
            password.append(character)

        random.shuffle(password)
        return ''.join(password)

if __name__ == "__main__":
    print(generate_password())