num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operation = input('Enter an operation: (eg.""+","-","*","/"") ')

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print('Invalid operation')