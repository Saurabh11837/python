# ----------- Dunder Mehtod -------------+
# What is Dunder Method?
# --> Dunder = Double Under (methods with __methodname__ )
# --> Special methoods in Python that start and end with double underscores
# --> They allow objects to  behave in special ways

# --> Dunder methods are special methods in Python that start and end with double underscores. Like "_init__","__str__","__add__", etc.
# --> They automatically get called when you perform certain actions on an object.
# They help you:
#   --> Customize behavior of your class
#   --> Make your class objects behave like built-in data types (like strings, lists, etc..)


# Example:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello how are you..! and your name is {self.name}"

    def __add__(self, other):
        # Combine names for fun
        new_name = f"{self.name} & {other.name}"
        # Combine ages
        new_age = self.age + other.age
        # Return a new Person object
        return Person(new_name, new_age)

obj = Person("Ravi..",18) 
obj2 = Person("Shivam",15) 
obj3 = Person("shiva",35) 

print(obj) 
print(obj+obj2) 
print( obj + ( obj2 + obj3))
# Output:
# Ravi..













