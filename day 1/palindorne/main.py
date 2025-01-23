# class palindrome:
#     def rev():
#         inp = input("Enter a number or string")
#         rev_inp = None
#         for i in inp:
#             rev_inp = i + rev_inp
        
#         if rev_inp == inp:
#             print(f"Input and output are palindrone")
#         else:
#             print("Input string is not palindrone")
    


# p1 = palindrome.rev()
# print(p1)

def rev_int():
    text = int(input("Enter a number "))
    rev = 0
    while text != 0:
        digit = text % 10
        rev = rev * 10 + digit
        text //= 10
    print(rev)
    

rev_int()