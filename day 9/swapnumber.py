# swapping numbers withot using third variable
# method one Using arithmatic operators

a = 10
b = 20
print("Using arithmatic operators")
print(f"Origin a={a} , b={b}")
a = a + b  # a becomes 30
b = a - b  # b becomes 10
a = a - b  # a becomes 20

print("After swapping: a =", a, ", b =", b)

# Method 2: Using Bitwise operator
a = a ^ b
b = a ^ b
a = a ^ b
print("Using Bitwise operator")
print("After swapping: a =", a, ", b =", b)

# Method 3: Using Python’s Tuple Unpacking

a = 10
b = 20

a, b = b, a  # Swapping in a single line
print("Using Python’s Tuple Unpacking")
print("After swapping: a =", a, ", b =", b)