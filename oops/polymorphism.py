# --------- Polymorphism ---------
# What is Polymorphism? 
# --> We can sysa Same name having different behavior, is called polymorphism.
# --> The same function or method name can work on different types of objects
# -->Polymorphism is a core concept in Object-Orinted Programming (OOP). The word means "many forms" -- and in programming it allows the same interface or method name to behave dirrerently depending on the object or context.

# Types of Polymorphism
# 1. Duck Typing (Implicit Polymorphism)
# 2. Method Overriding (Runtime Polymorphism)
# 3. Operator Overloading
# --> Polymorphism can achived in python in two ways if we talk about compile time languages there are 3 ways but python does not support Method overloading.
# --> Method overloading means having same name method inside a class but parameters will be different but in python the latest definition will overwrite the previous one.
# "Method Overriding"
#           -------> This is where a child clas overrides a method of the parent class, and Python decides at runtime which method to call, based on the object type.


# 1. Duck Typing :- Python dosen't care about the object type -- it care about wwhat the object can do.
# # Example:
# class Dog:
#     def speak(self):
#         print("Bark")

# class Cat:
#     def speak(self):
#         print("Meow")

# def make_sound(animal):
#     animal.speak()

# d = Dog()
# c = Cat()

# make_sound(d)
# make_sound(c)

# 👉 Output:
# Bark
# Meow


# 2. Method Overridng :- When a child class provides its own implementation of a method that is already defined in the parent class.
# # Example:Method overriding
# class Animal:
#     def show(self):
#         print("hellow I am aryan")
# class Human(Animal):
#     def show(self):
#         print("How are you")
    
# obj = Human()
# obj.show()

# OUTPUT:
# How are you

# 3. Operator Overloading: Means giving special meaning to operators( like +, -, *) for user-defined objects.
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):   # overloading +
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)

# 👉 Output:
# 30




























