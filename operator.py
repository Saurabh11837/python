# Operator in Python
# Types of Operators
# 1.Arithmetic Operators
# 2.Assignment Operators
# 3.Comparison Operators
# 4.Logical Operators
# 5.Identity Operators
# 6.Membership Operators
# 7.Bitwise Operators

# Examples of different data types operators in Python
# 1. Arithmetic Operators
# Types of Arithmetic Operators: +, -, *, /, %, **, //, ()

a = 10
b = 5
print(a+b)  # Output: 15 , Addition
print(a-b)  # Output: 5 , Subtraction
print(a*b)  # Output: 50 , Multiplication
print(a/b)  # Output: 2.0 , Division always returns a float
print(a%b)  # Output: 0, Modulus operator, gives remainder
print(a//b)  # Output: 2, Floor Division, divide karta hai but sirf ingeger part deta hai, eg. 5//2 =2.5 but ans-> 2,  
print(a**b)  # Output: 100000, Power / Exponent,

# | Category             | Data Types                         |
# | --------------------------------------------------------- | 
# | Arithmetic Operators | +, -, *, /, %, **, //, ()          |
# | Assignment Operators | =, +=, -=, *=, /=, %=, //=, **=    |
# | Comparison Operators | ==, !=, >, <, >=, <=               |
# | Logical Operators    | and, or, not                       |
# | Identity Operators   | is, is not                         |
# | Membership Operators | in, not in                         |
# | Bitwise Operators    | &, |, ^, ~, <<, >>                 |
# Explanation of each operator type can be found in the respective sections of the documentation.

# 2. Assignment Operators,
# Compund assignment operators combine a binary operation and an assignment in a single step.
x = 10
x += 5  # Equivalent to x = x + 5
x += 10 # Equivalent to x = x + 10
x += 15 # Equivalent to x = x + 15
# Now x = 10 + 5 + 10 + 15 = 40
print(x)  # Output: 40

x -= 3  # Equivalent to x = x - 3
print(x)  # Output: 37
x *= 2  # Equivalent to x = x * 2
print(x) # Output: 74

x /= 2 # Equivalent to x = x/2
print(x) #output 37

x %= 7 # Equivalent to x = x % 7
print(x) #output 2.0

x //= 1 # Equivalent to x = x // 1
print(x) #output 2.0

x **= 3 # Equivalent to x = x ** 3
print(x) #output 8.



# 3. Comparison Operators
# category | Operators | Description
# ----------------------------------------------------------
# Comparison Operators | ==, !=, >, <, >=, <=               |
#-----------------------------------------------------------

first_value = 10
second_value = 20

print(first_value == second_value)  # Output: False
print(first_value != second_value)  # Output: True
print(first_value > second_value)   # Output: False
print(first_value < second_value)   # Output: True
print(first_value >= second_value)  # Output: False
print(first_value <= second_value)  # Output: True




