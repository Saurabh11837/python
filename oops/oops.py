# ------- OPPs in Python -------
# OOPs stands for Object Oriented Programming System, it is a programming paradigm that uses "objects" to design applications and programs. It utilizes several techniques from previously established paradigms, including modularity, polymorphism, and encapsulation. OOPs is based on the concept of "objects", which can contain data in the form of fields (often known as attributes or properties) and code in the form of procedures (often known as methods).

# What is OOPs in Python?
# OOPs in Python is a programming paradigm that allows developers to create and manipulate objects, which are instances of classes. It provides a way to structure code in a more modular and reusable manner, making it easier to manage and maintain complex software systems. OOPs in Python supports features such as encapsulation, inheritance, and polymorphism, which enable developers to create flexible and scalable applications.

# For understanding OOPs first lets see what we were doing in python for creating a program of addtion we first use imperative approach.
# Imperative approach
# a=12
# b=13
# c=a+b
# print(c)  #Output: 25

# This approach is simple just se 2 variables and add them one problem with this is you have to make 2 other variables for adding 2 other numbers.

# Next approach is using function, to add 2 numbers this is function approach.
# def addItem(a,b):
#     return a+b

# print(addItem(12,13)) #Output: 25
# print(addItem(100,200)) #Output: 300

# Here the good thing is we can add multiple numbers without using multiple variables but still we have to call the function every time we want to add 2 numbers.


# --------------- OOPs Approach ---------------
# OOPs (Object Oriented Programming System) is a programming paradigm based on the concept of "objects", which can contain data(attributes) and code (methods).

# I know it is though to understand right now but it will be easy after learning there are many concepts that we have to learn like classes, objects, Encapsulation, Inheritance, Polymorphism, etc. 

# First will see how to create a class and object in python and then we will see the other concepts of OOPs in python.
# 1. What is class?
# --> A class is a blueprint or template for creating objects.
# --> Think of a class like the blueprint of a house. It definess what the house should have(rooms, windows, doors, etc.) btu dosen't build the house. An object is the actual house built using that blueprint.
# Syntax:
# --> A class is also created with a basic keyword class and a name in front of it.
# ------------- Example: -------------
# class Car:
#     brand = "Toyota"




# ->Creating a class super simple now lets see what is inside class. There are 2 type of things inside class Attributes and Methods.
# 1. Attributes: Variables defined inside the class are Attribute.
# 2. Methods: Functions defined inside a class are Methods.
# Why class name start with capital letter?
# --> It is a convention in Python to start class names with a capital letter. This helps to distinguish class name from variable and function names, which typically start with a lowercase letter. It also improves code readability and makes it easier to identify classes in the codebase.
# --> It is not mandatory to start class names with a capital letter, but it is a widely followed convention in the Python community. Following this convention can help improve the readability and maintainability of your code, especially when working on larger projects or collaborating with other developers.
# ------- Example -------
# class Animal:
#     species = "Dog"  #Attribute, Agar kisi variable ko class ke andar define karte hai to wo variable class ka attribute ban jata hai, aur uska value har object ke liye same hota hai.

#     def make_sound(self):  #Method, Agar kisi function ko class ke andar define karte hai to wo function class ka method ban jata hai, aur uska behavior har object ke liye same hota hai.
#         return "Woof! Woof!"
    
#     print("Hello how are you i am getting initialized")  #Ye print statement class ke andar hai to ye print statement class ke load hone par hi execute ho jayega, aur jab bhi class load hoga ye print statement execute hoga, chahe hum class ka object banaye ya na banaye.

# Øutput:
# Hello how are you i am getting initialized 

# Animal() #Output: Hello how are you i am getting initialized, (jab bhi class ka object banega to class load hoga to ye print statement execute ho jayega).

# If we want to use the attributes/variables outside the class.
# We can access these variables in two ways:
# 1. Using the class name:
# print(Animal().species)  #Output: Dog
# print(Animal().make_sound()) # ye line run kyu nahi kar rha hai? 


# # 2. Using the object of the class:
# animal = Animal() #Output: Hello how are you i am getting initialized, (jab bhi class ka object banega to class load hoga to ye print statement execute ho jayega).
# print(animal.species) #Output: Dog, 
# print(animal.make_sound())  #Output: Woof! Woof!


# ------ Object in Python ------
# What is object?
# --> An object is an instance of a class. It is a specific realization of a class that can have its own unique state and behavior. Objects are created from classes and can interact with each other through their methods and attributes. 
# Object Syntax
# --> It is very easy to create an object you just have to call the class inside a variable and that variable becomes an object.
# --> The object has ll the powers of a class therefore a classs object can access attributes and methods of a class.
# class fruit:
#     name = 'Apple'

# # Creatin an Object of the class fruit
# obj = fruit() 
# # Accesssing the attribute of the class with object.
# print(obj.name) #Output: Apple, (object f can access the attribute name of the class fruit)


# How many creating an object of a class is possible?
# --> We can create as many objects of a class as we want. Each object will have its own unique state and behavior, but they will all share the same attributes and methods defined in the class. For example:
# class Person:
#     species = "Human"

# Creating multiple objects of the class Person
# person1 = Person()
# person2 = Person()
# person3 = Person()
# person4 = Person()

# print(person1.species) #Output: Human
# print(person2.species) #Output: Human
# print(person3.species) #Output: Human
# print(person4.species) #Output: Human

# ---- What is constructor in Python? ----
# --> A constructor is a special method in a class that is automatically called when an object of the class is created. 

# Example of constructor in Python:
# class Factroy:

#     # self keyword target the location of the class object..
#     def __init__(self,material, zips, pockets):  #This also konwn as "default constructor" because it does not take any parameters other than self.ans this method also says as render method because it is used to render the object of the class.
#         print(self)
#         self.material=material
#         self.zips=zips
#         self.pockets=pockets

#     def show(self):
#         print(f"Your object details are {self.material} , {self.pockets}, {self.zips}")

# reebok = Factroy("Leather",3 , 4) 
# print(reebok.pockets)
# campus = Factroy("nylon",3,3)
# print(campus.pockets)

# reebok.show()






# ---------- Types of Attribute ------------
# Class attribute - A normal variable created inside a class but outside the method, that it.
# Instance attribute - A attribute created using and instance like self.name, self.age etc. It is known as instance attribute.

# Example:
# class Car:
#     wheels = 4  #Class attribute
#     def __init__(self, color):
#         self.color=color  #Instance Attribute
    
#     def show(self):
#         print(f"The car color is {self.color} and it {self.wheels} wheels")

# objCar = Car("red")
# objCar.show()


# ----- Type of Methods -------
# 1. Instance Method :- An instance method Works with instance (object) of the class. This method can access an modify instance attributes.
# # Example:
# class MyClass1:
#     def instance_method(self):
#         print(f"This is an instance method..")

# 2. Class Method :-This method works with the class itself it will not target the instance(object). we have to use @classmethod decorator for creating the class method and it takes cls as their first parameter.
# # Example:
# class MyClass2:
#     @classmethod
#     def class_method(cls):
#         print(f"This is a class method")
    
# 3. Static Method :- This method doesn;t access class or instance directly it alos uses a decorator @staticmethod it just acts like a regular function placed inside a class.
# # Example:
# class MyClass3:
#     @staticmethod
#     def static_method():
#         print(f"This ia a static method ")


# Example of every statement
class Animal:
    name = "Lion" #Class attribute

    def __init__(self,age):
        self.age = age #Instance attribute

    def show(self):
        print(f"How are you, Your age is {self.age}")

    @classmethod
    def hello(cls):
        print(f"How are you brother ")

    @staticmethod
    def static():
        print("How are you")

obj = Animal(12)

obj.show() #Output: How are you, Your age is 12
obj.hello() #Output: How are you brother
obj.static()  #Output: How are you





# ------------------------------------------------------------------------------------------------------------------------
# Output:
# <__main__.Factroy object at 0x000001D5593086E0>   #This is the location of first object
# 43
# <__main__.Factroy object at 0x000001D55930C550>     #This thhe location of second object
# 3
# OOPs Approach Example:
class Calculator:
    def __init__(self, a, b):
        print(a+b)

# Creating an object of the class Calculator
calc = Calculator(12, 13) #Output: 25


