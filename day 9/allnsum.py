# sum of all numbers from 1 to N

# Method 1: Using a for loop
N = int(input("Enter a number: "))
sum_number = 0

for i in range(1, N + 1):
    sum_number += i

print("Sum of numbers from 1 to", N, "is:", sum_number)


# Method 2: Using a while loop
i = 1
sum_numberss = 0
while i <= N: 
    sum_numberss += i
    i += 1 

print("Sum of numbers from 1 to", N, "is:", sum_numberss)


# Method 3: Using the formula (without a loop)

sum_numbers = (N * (N + 1)) // 2
print("Sum of numbers from 1 to", N, "is:", sum_numbers)
