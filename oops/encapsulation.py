# ------- Encapsulation ----------
# What is Encapsulation?
# --> Encapsulation means putting data(variables) and code(functions) together in one place - inside a class.
# --> It also meaans hiding the internal details aof how things work, and only showing what is needed.
# It keeps data safe from being changed by mistake. 
# It makes your code clean and easy to use.
# It gives control over what other can access or change.

# Access modifiers in Python
#  Access modifiers meanshow we give access of our attrbutes and methods to the object or inherited classes. There are 3 types lets see them one by one.
# 1. Public Attributes and Methods
#  --> Till now every attribute and methods we have created are pubic means the inherited clases and objects can access them no matter what.

# 2. Protected Attributes and Methods.
#   --> Python protected members are created using a single undescore but it still can be accessed from outside the class so you might wonder whats the point of using them. 
#   --> Python doesn't enforce protected access like other languate (e.g., Java or C++). But it uses a naming convertion to tell developers


# 3. Private Attribute and Methods
#   --> A private variable or method means:
#   --> It cannot be accessed from outside the cllass -- only from inside the class where it is defined.
#   --> In Python, we use two undrscores(__) before the name to make it private.






# # Example:public Access modifiers
# class Factory:
#     a = "pune"

#     def show(self):
#         print("Hello i am a pune factory")

# class Bhopal(Factory):
#     def show2(self):
#         print(super().a)

# obj=Bhopal()
# obj.show2()

# OUTPUT:
# pune

# Example:protected Access modifiers  ("_" if added before any attribute and method) these id protect reul apply
# # protected modifier same work as a public modifier in python, it is use to naming convention for developer
# class Factory:
#     _a = "pune"  #This is protected attribute

#     def _show(self):  #This is a protectd method
#         print("Hello i am a pune factory")

# class Bhopal(Factory):
#     def show2(self):
#         print(super()._a)

# obj=Bhopal()
# obj.show2()

#OUTPUT:
# pune

# # Example : private access modifire
# class Factory:
#     __a = "pune"  #This is protected attribute

#     def __show(self):  #This is a protectd method
#         print("Hello i am a pune factory")

# class Bhopal(Factory):
#     def show2(self):
#         print(super().__a)

# obj=Bhopal()
# obj.show2()

# OUTPUT:
# PS D:\python\oops> python encapsulation.py
# Traceback (most recent call last):
#   File "D:\python\oops\encapsulation.py", line 76, in <module>    
#     obj.show2()
#     ~~~~~~~~~^^
#   File "D:\python\oops\encapsulation.py", line 73, in show2       
#     print(super().__a)
#           ^^^^^^^^^^^
# ion.py", line 73, in show2       
#     print(super().__a)
# ion.py", line 73, in show2       
# ion.py", line 73, in show2       
# ion.py", line 73, in show2       
# ion.py", line 73, in show2       
# ion.py", line 73, in show2       
#     print(super().__a)
#           ^^^^^^^^^^^
# AttributeError: 'super' object has no attribute '_Bhopal__a'  


# # Example : Solution hai uppar wla program ka, kaise access karege private variable/attribue ko.
# class Factory:
#     __a = "pune"  #This is protected attribute

#     def show(self):  #This is a protectd method
#         print(f"Hello i am a {Factory.__a} factory")

# class Bhopal(Factory):
#     pass

# obj=Bhopal()
# obj.show()

# OUTPUT:
# Hello i am a pune factory

# # Example: private attribute uses.
# class Demo:
#     def __init__(self):
#         self.name="Public Mumber"  #Public
#         self._age = 21             #Protected
#         self.__salary = 5000       #Private

#     def show(self):
#         print("Inside the class:")
#         print("Public: ", self.name)
#         print("Protected: ", self._age)
#         print("Private: ", self.__salary)
    
# obj = Demo()
# obj.show()

# OUTPUT:
# Inside the class:
# Public:  Public Mumber
# Protected:  21
# Private:  5000

# Example:2
class Employee:
    __salary = 50000
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, amount):
        self.__salary = amount

e = Employee()
print(e.get_salary())  # 50000
e.set_salary(60000)
print(e.get_salary())  # 60000












