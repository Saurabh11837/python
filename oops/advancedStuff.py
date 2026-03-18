# ------------------- Decorator ---------------------
# --> Decorator is a function that wrap the another function.
# --> A decorator is just a function that modifies another function without changing its actual code.
# --> Imagine you have a cake (your function). A decorator is like putting icing on the cake. It doesn't charge the cake itself, but makes it bettwer, prettier, or adds some new flavor!
# --> For creating a decorator you first have to create a decorator function and then inside that we will create a wrapper.
#


# #Example:
# class Animal:
#     def show(self):
#         print("Hello, How are you!") 
    
#     @property   #Typicaaly This property  used to deal with property
#     def show1(self):
#         print("Hello how are you!")


# obj = Animal()
# obj.show()
# obj.show1


# Example 2
# def decorate(func):
#     def wrapper():
#         print("I will print my self before the function hello..")
#         func()
#         print("I will print after the function..")
#     return wrapper


# @decorate
# def hello():
#     print("Hello, I am akarsh..")

# hello()

# # Example:
# def middleware(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper


# @middleware
# def hello():
#     print("Hello")

# hello()

# # Example:Real world example 
# def auth(func):
#     def wrapper(user):
#         if user == "admin":
#             func(user)
#         else:
#             print("Unauthorized")
#     return wrapper


# @auth
# def dashboard(user):
#     print(f"Welcome {user}")

# dashboard("admin")
# dashboard("guest")


# # Access prameter wiht decorator function

# def middleware(func):
#     def wrapper(a,b):
#         print("the addtion to your numbers are ")
#         func(a,b)
#         print("Thankyou I hope you liked it ")
#     return wrapper

# @middleware
# def addtion(a,b):
#     print(f"The addtion is {a+b}")

# addtion(10,5)

# OUTPUT:
# the addtion to your numbers are 
# The addtion is 15
# Thankyou I hope you liked it



# -------------  *args & **kwargs  -------------

# --> For making the decorator with Arugments it is tough for this we will move towards out next advanced stuff *args, **kwargs.

# What is Args and Kwargs?
# --> They are special keywords in python used in function definitions to accept a flexible number of arguments.
# --> Now you always dont't have to use Args and Kwargs the main thing is *, ** you can use any name in front of them.
# --> So *args are used for multiple positional arguments, and **kwargs are used for multiple key word arugments.
# --> And the *args becomes a tuple and **kwargs become a dictionary.
# --> The use case is great.
#     You don't need to know how many inputs you'll get.
#     Helps in bulding flexible functions, decorators, APIs and more.


# Example: Args
# # In function/method store number of argument with one "*"star it was store in tuple formet.s
# def addition (*args):  
#     print(args)
#     sum=0
#     for i in args:
#         sum += i
    
#     print(f"sum of all number : {sum}")

# addition(12,23,34,45,56)

# OUTPUT:
# (12, 23, 34, 45, 56)
# sum of all number : 170




# Example: **kwargs (means keyword arguments).
# isme jo data aa raha hai wo key basis pe save ho rah hai ye nahi ki jo first me ha wo first arugment ka data sotre karega, aur last wala arugment last ka data store kare.
## Yaha data sote key ke basis pe hota hai
# def addtion(b, c, a):
#     print(f"A : {a}")
#     print(f"B : {b}")
#     print(f"C : {c}")
#     print(a+b+c)

# addtion(c=10,a=12,b=15)

# OUTPOT:
# A : 12
# B : 15
# C : 10
# 37

# Example: agar multiple keys ho parameter me aaye to handle karne ke liye "**kwargs" ka use karenge, ye data key ke basis pe store karta hai
# def information(**kwargs):
#     print("Your information.. ")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# information(name="Akarsh", age=23, designation = "AI/ML")

# OUTPUT:
# Your information.. 
# name : Akarsh
# age : 23
# designation : AI/ML


# # ---- Args  &  Kargs uses in decorator function ----------
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("The addtion to your number are : ")
#         func(*args,**kwargs)
#         print("Thank you I hope you Liked it..")

# def addtion(a,b):
#     print(a)
#     print(b)
#     print(f"Your total is  {a+b}")

# addtion(55,55)

## Example:
# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()

#         result = func(*args, **kwargs)

#         end = time.time()
#         print("Execution time:", end - start)

#         return result

#     return wrapper


# @timer
# def add(a, b):
#     time.sleep(1)   # delay for demo
#     return a + b


# output = add(2, 3)
# print("Result:", output)


# OUTPUT:
# Execution time: 1.0003786087036133
# Result: 5


# ===========================================================
# List, Dictionary and set comphrehension

# When we use of this
# 👉 List → jab ordered data chahiye
# 👉 Dict → jab mapping chahiye
# 👉 Set → jab unique data chahiye
# What is Comprehension?
# --> Comprehension = short & clean way to create collections (list, dict, set)
# ===========================================================
# -->All of the Comprehension are used to create List, Dictionary and set. But you don't have to use multiple lines of code for loops and if-Else statements.


# Example:
# Instead
# result = []
# for x in range(5):
#     result.append(x)

# We can write as it
# result = [x for x in range()]

# ****************** List Comprehension ******************
# Syntax:
# [variable, loop, condition]
#       or
# [variable, condition, loops]

# [expression for item in iterable if condition ]
# 
# labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
# labels1=[i for i in range(1,21) if i % 2 == 0]
# print(labels1)
# print(labels)


# OUTPUT:
# ['Even', 'Odd', 'Even', 'Odd', 'Even']

## Example 2:
# marks = [45, 78, 90, 33]
# result = ["Pass" if m >= 40 else "Fail" for m in marks]
# print(result)

# **** Dictionary Comprehension ****
# Syntax:
# {key: value for item in iterable if condition}

# # Example:
# evenSquare = {x: x*x for x in range(10) if x % 2 == 0}
# print(evenSquare)

# # OUTPUT:
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


# # Example 2:
# users = ["Akarsh", "Rahul", "Aman", "Aryan", "Raj"]
# user_dict = {user: len(user) for user in users}
# print(user_dict)

# # OUTPUT:
# {'Akarsh': 6, 'Rahul': 5, 'Aman': 4, 'Aryan': 5, 'Raj': 3}



# **********************  SET Comprehension  **********************


# Syntax:
# {expression for item in iterable if condition}

# # Example:
# unique_evne_squares = {x*x for x in range(10) if x % 2 == 0}
# print(unique_evne_squares)


# # OUTPUT:
# {0, 64, 4, 36, 16}


# emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]

# unique = {email for email in emails}
# print(unique)

# OUTPUT:
# {'a@gmail.com', 'b@gmail.com'}


# =============================================================================
# What is Lambda Function?
# Lambda function = anonymous, short, inline function in python
# --> A lambda function is an anonymous,  inline function defined using the lambda keyword.
# --> It's often used for short, simple function that are used only once or temporally.
# --> You can have multiple arguments but there will be only one expression.
# --> It's a one-liner function without a name.
# --> Used for small functions you need just once.
# Syntax:
# lambda arguments : expression

# --> Takes any number of arguments
# --> Returns the value of the expression (no explicit return needed)
# =============================================================================
# Example:
# addtion = lambda a,b : a+b
# print(addtion(10,20))

# Example:
# evenOrOdd = lambda a: "even" if a % 2 == 0 else "odd"
# print(evenOrOdd(5))
# print(evenOrOdd(8))




# Example1: Suppose you have a list of tuples (name, age) and want to sort by age.

# people = [("Akarsh", 21), ("Rahul",24),("Aryan", 19)]
# # Sort by age
# people_sorted = sorted(people, key=lambda person: person[1])

# print(people_sorted)

# # OUTPUT:
# [('Aryan', 19), ('Akarsh', 21), ('Rahul', 24)]

# # Example 2: Filtering even numbers from a list
# nums = [1,2,3,4,5,6]

# evens = list(filter(lambda x : x % 2 == 0, nums))
# evens1 = list(filter(lambda x : print(x), nums))
# print(evens)
# print(nums)

# OUTPUT:
# 1
# 2
# 3
# 4
# 5
# 6
# [2, 4, 6]
# [1, 2, 3, 4, 5, 6]


# # Example 3: Square each number in list
# nums= [1,2,3,4]

# square = list(map(lambda x: x*x, nums))
# print(nums)
# print(square)


# =================================================================================
#                       Module and packages
# 
# What is Module in Python?
# --> Module is just a single file containting code and we can use this file code in other file.
# --> A single Python file (.py)
# --> Contains functions, variables, or classes
# --> Use to organize and reuse code
# --> Python comes with lots of ready-to-use modules like:
#   * math (for math operations)
#   * random (for generating random number)
#   * datetime (for date and time)
# =================================================================================










































