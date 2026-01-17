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

# check comprasion in ASSCI values
print(ord("A")) # ASSCI value of "A" Output: 65
print(ord("B")) # ASSCI value of "B" Output: 66
print("A" < "B") # Output: True, because 65 < 66
print("A" > "B") # Output: False, because 65 > 66
print("ABC"> "ACD") # Output: False, because at index 1 'B'(66) < 'C'(67)
print("ABC"< "ACD") # Output: True, because at index 1 'B'(66) < 'C'(67)



# 4. Logical Operators
# category | Operators | Description
# ----------------------------------------------------------
# Logical Operators    | and(&), or(||), not(!)                       |
#-----------------------------------------------------------

# Logical AND Operator Example
print(123> 100 , 34 == 34) #Output is : True True, but is not right way
# So here using logical condition and operator
print(123>100 and 34==34) # if all condition is true then the ans is "True", if one of any coditio is false the the ans is false
print(123>100 and 34==34 and "A"=="A" and 125==125) 
print(123>100 and 34==34 and "A"=="A" and 125==126) # if all condition is then the ans is "True"

# "or" operator
# Logical OR Operator Example
# if one condition is true then the ans is true
print(123>100 or 34==35) #Output is : True
print(123<100 or 34==35) #Output is : False
print(12!=12 or 23==45 or 53>23 or 45==45) #Output is : True

# "not" operator
# Logical NOT Operator Example
# it reverse the condition,
# jo bhi condition hoga uska opposite dega, agar condition true hoga to not operator false dega, agar condition false hoga to not operator true dega.
print(not(123>100)) #Output is : False
print(not(123<100)) #Output is : True

# 5. Identity Operators
# category | Operators | Description
# ----------------------------------------------------------
# Identity Operators   | is, is not                         |
#-----------------------------------------------------------

# Identity Operators Example
# "is" operator
# "is" operator ka use hota hai do variable ka memory address check karna. dono variable ka memory address same hai ya nahi.
#  "is not" operator ka use hota hai ki do variable ka memory address same nahi hai na, ye check karta hai.
# isme do variable ka memory address check karta hai, agar dono variable ka memory address same hoga to ans true dega, agar alag hoga to false dega.
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # Output: True
print(a is c)  # Output: False
print(a is not c)  # Output: True

# 6. Membership Operators
# category | Operators | Description
# ----------------------------------------------------------
# Membership Operators | in, not in                         |
#-----------------------------------------------------------
# Membership Operators Example
# "in" operator
# "in" operator ka use hota hai check karne ke liye ki koi value kisi sequence (like list, tuple, string) mein exist karti hai ya nahi.
# "not in" operator ka use hota hai check karne ke liye ki koi value kisi sequence mein exist nahi karti hai.
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print("grape" in fruits)   # Output: False
print("grape" not in fruits)  # Output: True
print("apple" not in fruits)  # Output: False

# 7. Bitwise Operators
# category | Operators | Description
# ----------------------------------------------------------
# Bitwise Operators    | &, |, ^, ~, <<, >>   
# & operator performs bitwise AND operation 
# | operator performs bitwise OR operation
# ^ operator performs bitwise XOR operation
# ~ operator performs bitwise NOT operation
# << operator performs left shift operation
# >> operator performs right shift operation
#-----------------------------------------------------------
# Bitwise Operators Example
a = 10  # In binary: 1010
b = 4   # In binary: 0100
print(a & b)  # Output: 0 , Bitwise AND
#   1010           
# & 0100      
# ------       
#   0000      
# --> Output: 0 ,Bitwise AND

print(a | b)  # Output: 14 , Bitwise OR
# Bitwise OR  
#     1010     
#   | 0100
#    ------
#     1110
#  output: 14
#  Bitwise OR

print(a ^ b)  # Output: 14 , Bitwise XOR
# ^ operator performs bitwise XOR operation
#   1010           
# ^ 0100      
# ------       
#   1110         
# --> Output: 14 , Bitwise XOR     

# `~` operator performs bitwise NOT operation
print(~a)  # Output: -11 , Bitwise NOT
# Bitwise NOT
#   1010
#  ------
#   0101 (This is one's complement)
#  To get two's complement, add 1
#   0101
# +    1
# ------
#   0110
#  output: -11 (in two's complement representation)

# `<<` operator performs left shift operation
print(a << 2)  # Output: 40 , Left Shift
# Left Shift
#   1010 << 2
# = 101000
# Output: 40

# `>>` operator performs right shift operation
print(a >> 2)  # Output: 2 , Right Shift
# Right Shift
#   1010 >> 2
# = 0010
# Output: 2






# Some practice question
# print(126>130) #False
# print((456==456)!=(235==236)) #True
# print(2<10 or 45==56 or 69>70 or 15!=13) #True
# print(True and bool(0)) #False