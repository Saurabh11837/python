# Function in Python
# A function is a block of reusable code that performs a specific task.
# It reduces repetition
# Makes code organized and readable

# Syntax
# def function_name(parameters):
#     # code block
#     return value  # optional

# Example:
# 1.
# def message(n):
#     for i in range(1,n,1):
#         print("Hello function")

# message(5)
# def sum(a,b):
#     print(f"The sum of two numebr is {a+b}");



# Types of Arugments pass in the function
# Now there are 3 types of arugment that we can pass to parameters. positional arugment, default arugment, keyword arugment, For understandd the we will first see examples.
# ========== Type 1(passing arugment in funciton) ===========
# sum(5,6)
# def add(a, b):
#     return a + b

# print(add(5, 3))  # Output: 8

# ========== Type 2(passing arugment in funciton) ===========
# Here passing keyword arugmet
# def introduce(name,age):
#     print(f"I am {name} and I am {age}, years old.")

# introduce(age=22,name="Saurabh")

# ========== Type 3(passing arugment in funciton) ===========
# def greet(name="Guest"):
#     print(f"Hello, {name}")

# greet()
# greet("Saurabh")

# Define a function to check to palindrom

# def palindron(str):
#     rev=""
#     for i in range(len(str)-1,-1,-1):
#         rev=rev+str[i]
    
#     if rev == str:
#         print("Palindrom")
#     else:
#         print("Not Palindrom")

# palindron("NAMAN")
# palindron("saurabh")

# function through return some data.
def hello():
    return "Hii Saurabh.."

print(hello())
