print("Hello, World!")

#comment in python
#hey i am saurabh //Single lin comment
"""Hii saurabh this is 
multi line comment
"""

#variable in python
#variable name should not start with number
#variable name should not contain special character except e.g.: @,$,!,%,^,&,*
#variable name should not be a keyword

sher ="harsh fournder of sheryiian ai school"
a=12

# Naming convenstions in python three ways to write variable names
# 1.camel case
myNameIsSaurabh = "saurabh"
# 2.pascal case
MyNameIsSaurabh = "saurabh"
# 3.snake case
my_name_is_saurabh = "saurabh"
#data types in python
#1.string
name = "saurabh"

#Three type of number data type in python
#1.complex, 2.integer, 3.float
#1.complex
# Numbers with a real and an imaginary part
# Written using j for the imaginary unit

complex_number = 3 + 4j
c1 = 2 + 3j
c2 = -1j
c3 = 5j
print(c1.real)  # Output: 2.0
print(c1.imag)  # Output: 3.0
# Addition of complex numbers
sum_complex = c1 + c2  # (2 + 3j) + (-1j) = 2 + 2j
print("Complex number addtion: ",sum_complex)  # Output: (2+2j)
#2.integer
age = 21
#3.float
height = 5.9
#p/q this formet is called as rational number that is also called as fraction or floating point number
c=12/4

#4.boolean
is_student = True
is_student=False
#5.list
fruits = ["apple", "banana", "cherry"]
#6.tuple
coordinates = (10.0, 20.0)
#7.dictionary
person = {"name": "saurabh", "age": 21}
#8.set
unique_numbers = {1, 2, 3, 4, 5}
#type function
print(type(name))
print(type(complex_number))
print(type(age))
print(type(height))
print(type(c))
print(type(is_student))
print(type(fruits))
print(type(coordinates))
print(type(person))
print(type(unique_numbers))
#input function

# String type conversion
a = "A"
print(ord(a))  # Output: 65, ASCII value of 'A', converts character to integer using ord function
b=65
print(chr(b))  # Output: 'A', converts integer to character using chr function

# 
# | Category | Data Types                         |
# | -------- | ---------------------------------- |
# | Numeric  | `int`, `float`, `complex`, `bool`  |
# | Sequence | `str`, `list`, `tuple`             |
# | Mapping  | `dict`                             |
# | Set      | `set`, `frozenset`                 |
# | Binary   | `bytes`, `bytearray`, `memoryview` |
# | None     | `NoneType`                         |


# String Data Type accessing through indexing
a="Hello brother";
print(a[1]); #prints e
print(a[-1]); #prints r

# String Slicing
b="Hello brother";
# method of string slicing 
# eg. b[start:end:step]
print(b[0:5]); #prints Hello
print(b[6:13]); #prints brother
print(b[0:13:1]); #prints Hello brother
print(b[0:13:2]); #prints Hlobohr
print(b[0:13:3]); #prints Hlbtr
print(b[:5]); #prints Hello
print(b[6::]); #prints brother
print(b[::]); #prints Hello brother


# Type Conversion
a=12 #int
print(type(a))
a=str(a) #converted to string
print(type(a))
b=12.5 #float
print(type(b))
b=int(b) #converted to int
print(type(b))

# Boolean Type Conversion
x = 0
y = 5
print(bool(x))  # Output: False
print(bool(y))  # Output: True
# In Python, the following values are considered False in a boolean context:
# - `None`
# - `False`
# - Numeric zero values: `0`, `0.0`, `0j`
# - Empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `frozenset()`
# All other values are considered True.


# Input and Output
name = "Saurabh"
age = 45
# Normal way of printing output
print("Hello my name is ", name ," and my age is ", age)
# Using f-strings for formatted output 
print(f"my name is {name} and my age is {age}");

# user input function to take input from user
user_name= input("Enter your name: ")
user_age=int(input("Enter your age: "))
print(f"Hello {user_name}, your age is {user_age} !");