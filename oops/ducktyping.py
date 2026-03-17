# ------------ Duck Typing  ------------ 
# In Python, Duch Typing is a concept of polymorphism where:
# --> The type of object is not important
# --> What matters is the behavoir (method) the object has.

# ---- Simple Defination -----
# --> If is looks like a duch and behaves like a duck, it is a duck.
# That means
# --> Python does NOT check the class/type
# --> It checks whether the required method exists.


class Duck:
    def sound(self):
        print("Quack")

class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()

d = Duck()
g = Dog()

make_sound(d)
make_sound(g)

# OUTPUT:
# Quack
# Bark


