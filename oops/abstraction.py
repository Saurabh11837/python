# ------------- Abstraction -------------
# What is Abstraction:
# --> abstraction means, Hiding implementation details and showing only essential features.
# --> Abstraction does not exist in python but we can achive it using a library we will see what is a libary later.
# --> Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details.
# --> It is used to define a common interface for different subclasses.

# Abstract classes and methods
# --> Abstract classes are classes that contains one or more abstract methods.
# --> A method that is defined but not implemented in the abstract class. subclasses must provide the implementation.

# # Example:1
# abc Module

# 1. abc = Abstract Base Class module
# Built-in Python module
# Provides tools to define abstract classes and methods
# Helps enforce abstraction in Python
# 2. ABC Class
# ABC is a base class for defining abstract classes
# Any class that inherits from ABC becomes an abstract class

# from abc import ABC, abstractmethod

# class abstract(ABC):
#    --> Abstract methods have no body (implementation in child class)
#     @abstractmethod    #it is used to declare a method as abstract
#     def perimeter(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self,side):
#         self.side=side

#     def perimeter(self):
#         print("I have created ")

#     def area(self):
#         print("I have created")

# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius = radius
    
#     def perimeter(self):
#         print("I have created ")

#     def area(self):
#         print("I have created")

# obj = Circle(7)

# # Example : 2
# from abc import ABC, abstractmethod    #This line used to create abstract classes and method in Python.

# class Payment(ABC):
    
#     @abstractmethod
#     def pay(self):
#         pass

# class UPI(Payment):
#     def pay(self):
#         print("Paid using UPI")

# class Card(Payment):
#     def pay(self):
#         print("Paid using Card")

# def process(payment):
#     payment.pay()

# process(UPI())
# process(Card())

# OUTPUT:
# Paid using UPI
# Paid using Card




































