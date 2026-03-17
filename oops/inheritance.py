# Type of inheritance.

# Multipla Inheritance Problem 
# Diamond Problem in Python – Step by Step
# 1️⃣ Problem Setup

# Diamond Problem tab hota hai jab:

#       A
#      / \
#     B   C
#      \ /
#       D

# A = Grandparent class
# B and C = Parents (inherit from A)
# D = Child (inherits from B and C)
# Agar A me koi method hai, aur B & C me override hua, to D call kare to ambiguity hoti hai ki kaunsa method execute hoga?
# # 2️⃣ Python Code Example
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):
#     pass

# obj = D()
# obj.show()
# # 3️⃣ Step 1 – Check Method Resolution Order (MRO)
# Python internally C3 Linearization ka use karta hai to calculate D ka MRO:

# print(D.mro())

# Output:
# [D, B, C, A, object]

# Explanation:
# D → child class
# B → left parent first
# C → right parent next
# A → common grandparent

# object → Python base class

# ✅ C3 Linearization ensures:
# Child comes before parents
# Left-to-right parent order preserved
# No duplicate classes in search path

# 4️⃣ Step 2 – Method Lookup

# obj.show() #call karte hain:

# Python check karta hai D → show() nahi mila

# Fir B → show() mila → execute B ka show()

# C aur A check nahi kiye jaate, kyunki method mil chuka

# Output:

# B

# 💡 No ambiguity! Python auto-resolved using MRO.

# -------------------------------------------------------------------------------------------------------
# Keyword	        Use
# pass	    -->   kuch nahi karta (Use hota hai empty class, function, loop run ke liye etc.)
# Example:
# class Calculator:

#     def add(self):
#         pass

#     def subtract(self):
#         pass


# break	    -->   loop ko completely stop karta
# continue	-->   current iteration skip karta


# What is Inheritance?
# --> Inheritace Python OOp ka ek important  concept hai jiseme ek class dusri class ke properties aur methods ko inherit(use) kar sakti hai.
# In simple word
# "Parent class(Base class)" --> jis class se features milte hain
# "Child class (Derived class)" --> Jo class un features ko use karti hai.
# Isse code reuse hota haiaur program chhota aur clean ban jata hai.

# ----> Inheritance allows a class(child class) to inherit properties and behaviors (attributes and methods) from another class (parent class).
# Benefits of using inheritance is 
#   1. Code reusability
#   2. Organized structure
#   3. Easy to maintain and extend.

# Example:
# class Factory1:         # Parent/super class
#     a = "I am an attribute mentioned inside Factory1"
#     def hello(self):
#         print("Hello I am a method mentioned inside Factory1")
    
# class Factory2(Factory1): #Child/sub class
#     pass

# # Creatin object for first class
# obj1=Factory1()
# obj1.hello()
# print(obj1.a)


# # Creating object for second class
# obj2=Factory2()
# obj2.hello()
# print(obj2.a)

# ---> constructor inheritance
# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(f"Hello your name is {self.name}")

# class Human(Animal):
#     pass

# person1 = Human("Abhi")
# person1.show()


# Using the "super()" keyword
# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(f"Hello your name is {self.name}")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age
#     def show(self):  #same method in parent and child class but different behavior is called method over riding
#         print(f"Hello your name is {self.name}, And age is {self.age}")


# animal1 = Animal("lion")
# animal1.show()

# person1=Human("Abhi",23)
# person1.show()

# **************************************************************************************************
# Type of Inheritance
# 1. Single Inheritanc
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritace
# 5. Hybrid Inheritance
# **************************************************************************************************

# *********  1. Single Inheritace *********
# --> Ek parent class se ek child class inherit karti hai,
# *---> Single Inheritance is a type of inheritance, where one child class inherits from only one parent class, allowing the child class to reuse the properties and methods of that parent class.
# Example:1
# class A:
#     def show(self):
#         print("Class A")
    
# class B(A):
#     pass

# obj = B()
# obj.show()

# OUTPUT: Class A

# Example 2:
# Real-time Idea

# Employee → Developer
# Developer bhi ek employee hi hota hai.

# class Employee:

#     def work(self):
#         print("Employee works in company")


# class Developer(Employee):

#     def code(self):
#         print("Developer writes code")


# d = Developer()

# d.work()     # inherited method
# d.code()     # own method

# OUTPUT:
# Employee works in company
# Developer writes code

# *********  2. Multiple Inheritace *********
# --> Ek child class multiple parent classes se inheerit karti hai.
# -*-> Multiple Inheritance is a type of inheritance where a child class inherits from more than one parent class.
# Example:
# class A:
#     def showA(self):
#         print("Class A Execute")

# class B:
#     def showB(self):
#         print("Class B Execute")
    
# class C(A, B):
#     pass

# obj = C()
# obj.showA()
# obj.showB()

# OUTPUT:
# Class A Execute
# Class B Execute

# Example 2:
# class Father:
#     def skills(self):
#         print("Father: Gardening")

# class Mother:
#     def talents(self):
#         print("Mother: Cooking")

# class Child(Father, Mother):
#     def hobbies(self):
#         print("Child: Playing")

# obj = Child()

# obj.skills()
# obj.talents()
# obj.hobbies()

# Output:
# Father: Gardening
# Mother: Cooking
# Child: Playing

# Example 3:
# class A:
#     def show(self):
#         print("Class A")

# class B:
#     def show(self):
#         print("Class B")

# class C(A, B):
#     pass

# obj = C()
# obj.show()

# Python left-to-right order follow karta hai.
# print(C.mro())  #MRO --> Method Resolution Order, MRO ka matlab hai Python ka woh order jisme Python classes ko search karta hai jab koi method call hota hai, especially jab multiple inheritance use ho.


# # Example 4:
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")
# class C(A):
#     def show(self):
#         print("C")
# class D(B,C):
#     pass

# obj = D()
# obj.show()
# print(D.mro())

##--> Python internall C3 Linearization use karta hai jo ek algorithm hai jo Python (since Python 2.3) Multiple Inheritance me MRO calculate karne ke liye use karta tha.

# OUTPUT:
# Class A
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]


# *********  3. Multilevel Inheritace *********
# --> Inheritance chain me hota hai.
# --*--> Multilevel inheritance is a type of inheritance in Python where a class(child) inherits form anther class (parent), which itself inherits from another class (grandparent), forming a chain of inheritance.
# 1. It creates a grandparent --> parent --> child relationship.
# 2. Mehtods and attributes are inherited down the chain.
# 3. Each derived class can add or override functionality.
# Hierarchy Representation:

# GrandparentClass
#        ↓
#    ParentClass
#        ↓
#    ChildClass


# # Example:
# class Grandparent:
#     def greet(self):
#         print("Hello from Grandparent")

# class Parent(Grandparent):
#     def greet_parent(self):
#         print("Hello from Parent")

# class Child(Parent):
#     def greet_child(self):
#         print("Hello from Child")

# # Testing
# c = Child()
# c.greet()         # Inherited from Grandparent
# c.greet_parent()  # Inherited from Parent
# c.greet_child()   # Defined in Child

# Output:
# Hello from Grandparent
# Hello from Parent
# Hello from Child

# OUTPUT:
# Class A Execute
# Class B Execute
# Class C Execute

# Example: 2
# ---> Real-World Program – Bank Account Example
# Suppose we model a Bank System:
# Account → Grandparent class (basic info, deposit/withdraw)
# SavingsAccount → Parent class (specific features: interest)
# PremiumAccount → Child class (extra features: cashback, premium support
                              
# # Grandparent class
# class Account:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance

#     def deposite(self, amount):
#         self.balance += amount
#         print(f"{amount} deposited. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"{amount} withdrawn. Remaining balance: {self.balance}")
#         else:
#             print("Insufficient balance")

## Parent Class
# class SavingsAccount(Account):
#     def __init__(self, name, balance):
#         super().__init__(name, balance)
#         self.cashback = 0  # attribute for cashback
#     def add_interest(self):
#         interest = (self.balance * 5) / 100
#         self.balance += interest
#         self.cashback += interest  # keep track of cashback
#         print(f"Interest added: {interest}. New balance: {self.balance}")

#     def account_detail(self):
#         print("********* Account Detail ********* ")
#         print(f"Name : {self.name}")
#         print(f"Account Balance : {self.balance}")
#         print(f"Cashback of your Account balance : {self.cashback}")



## Child class
# class PremiumAccount(SavingsAccount):
#     def apply_cashback(self):
#         self.balance += self.cashback
#         print(f"Cashback {self.cashback} added. New balance: {self.balance}")
#         self.cashback = 0  # reset cashback after applying

# # Test
# p=PremiumAccount("Aryan Patel",1000)

# test=bool(True)
# while(test):
#     print("\nn1. For Creating Account :- ")
#     print("2. For Show account detail :- ")
#     print("3. For Deposite amount in Account :- ")
#     print("4. For Withdraw amount in Account :- ")
#     print("5. For Show the cash back amount in Account :- ")
#     print("6. Exit :- ")
#     choice = int(input("Enter your choice :- "))
#     match choice:
#         case 1:
#             name=str(input("Enter your name : "))
#             amount=float(input("Enter deposite amount : "))
#             PremiumAccount(name,amount)
#             p.add_interest()
            
#         case 2:
#             p.account_detail()
            
#         case 3:
#             amount=float(input("Enter your deposite amount : "))
#             p.deposite(amount)
            
#         case 4:
#             withdrawAmount=float(input("Enter your ammount which you want Withdraw :- "))
#             p.withdraw(withdrawAmount)
            
#         case 5:
#             p.apply_cashback()
            
#         case 6:
#             test=False
            
#         case _:
#             print("Invalid Choise ")


# # Example:
# class Factory:
#     def __init__(self,material, zips):
#         self.material=material
#         self.zips=zips
    
# class BhopalFactory(Factory):
#     def __init__(self, material, zips,color):
#         super().__init__(material, zips)
#         self.color=color

# class PuneFactory(BhopalFactory):
#     def __init__(self, material, zips, color, pockets):
#         super().__init__(material, zips, color)
#         self.pockets=pockets
    
#     def show(self):
#         print(f"Material : {self.material} \nZips : {self.zips} \nColor : {self.color}\nPockets : {self.pockets}")

# obj = PuneFactory("Polister",4,"Yellow",5)
# obj.show()       

#OUTPUT:
# Material : Polister
# Zips : 4
# Color : Yellow
# Pockets : 5    


# *********  4. Hierarchical Inheritace *********
# --> Ek Parent class se multipal child classes inherit karti hain.
# Key points:
# 1. Parent ka code reuse hota hai multiple child classes me
# 2. Har child class independent behavior bhi define kar sakti hai
# 3. MRO simple hota hai kyunki ek parent → multiple children
# Example:1
# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# --- Structure ---
#         Parent
#        /   |   \
#   Child1 Child2 Child3

# Example 2:
# # Parent class
# class Vehicle:
#     def __init__(self,brand):
#         self.brand=brand
    
#     def start(self):
#         print(f"{self.brand} vehicle started.")
# # child class 1
# class Car(Vehicle):
    
#     def fuel_type(self):
#         print(f"{self.brand} car uses petrol or diesel.")

# # child class 2
# class Bike(Vehicle):
#     def fuel_type(self):
#         print(f"{self.brand} bike uses petrol.")

# # child class 3
# class Truck(Vehicle):
#     def fuel_type(self):
#         print(f"{self.brand} truck uses diesel. ")

# # Test
# v1=Car("Toyota")
# v2=Bike("Honda")
# v3=Truck("Volve")

# v1.start()
# v1.fuel_type()

# v2.start()
# v2.fuel_type()

# v3.start()
# v3.fuel_type()

#OUTPUT:
# Toyota vehicle started.
# Toyota car uses petrol or diesel.
# Honda vehicle started.
# Honda bike uses petrol.
# Volve vehicle started.
# Volve truck uses diesel.

# Example:
# Real-World Example –-->Bank Account Types
# Suppose Bank has different account types:
# Account → Parent class
# SavingsAccount → Child1
# CurrentAccount → Child2
# FixedDepositAccount → Child3

# # Parent class
# class Account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def show_balance(self):
#         print(f"{self.name} has balance: {self.balance}")

# # Child class 1
# class SavingsAccount(Account):
#     def add_interest(self, rate=5):
#         self.balance += self.balance * rate / 100
#         print(f"Savings account balance after interest: {self.balance}")

# # Child class 2
# class CurrentAccount(Account):
#     def cheque_facility(self):
#         print(f"{self.name} can use cheque facility in current account.")

# # Child class 3
# class FixedDepositAccount(Account):
#     def maturity_amount(self, years, rate=6):
#         amount = self.balance * ((1 + rate/100) ** years)
#         print(f"FD maturity amount after {years} years: {amount:.2f}")

# # Test Program
# s = SavingsAccount("Aryan", 1000)
# c = CurrentAccount("Rohan", 5000)
# f = FixedDepositAccount("Meera", 20000)

# s.show_balance()
# s.add_interest()

# c.show_balance()
# c.cheque_facility()

# f.show_balance()
# f.maturity_amount(3)

# OUTPUT
# Aryan has balance: 1000
# Savings account balance after interest: 1050.0
# Rohan has balance: 5000
# Rohan can use cheque facility in current account.
# Meera has balance: 20000
# FD maturity amount after 3 years: 23820.32

# *********  5. Hybrid Inheritace *********
# --> Different inheritance types ka combination.
# --*--> Hybrid inheritance is a combination of two or more types of inheritance(single, multipe, multilevel, or hierarchical) in a single program.
#  1. It allows Python developers to reuse code from multiple inheritance pattern in a single class hierarchy.
#  2. Python solves method resolution conflicts using MRO(C3 Linearization) automitically.

# Hierarchy Example:
        #   A
        #  / \
        # B   C
        #  \ /
        #   D
        #   |
        #   E

# --> This combines Multiple inheritance (B + C -> D) Multilevel inheritance (D -> E) --> Hybrid inheritance
# Example: Multiple + Multilevel

# Real-World Example – Bank System
# Suppose a bank has:
# Account → Base class (common methods like deposit/withdraw)
# SavingsAccount → Inherits from Account
# SpecialAccount → Adds features like cashback, inherits from Account
# PremiumAccount → Combines SavingsAccount + SpecialAccount

# # Base class
# class Account:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} deposited. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"{amount} withdrawn. Remaining balance: {self.balance}")
#         else:
#             print("Insufficient balance")


# # Parent 1
# class SavingsAccount(Account):
#     def add_interest(self, rate=5):
#         interest = self.balance * rate / 100
#         self.balance += interest
#         print(f"Interest added: {interest}. New balance: {self.balance}")


# # Parent 2
# class SpecialAccount(Account):
#     def apply_cashback(self, cashback_amount):
#         self.balance += cashback_amount
#         print(f"Cashback {cashback_amount} applied. New balance: {self.balance}")


# # Child class → Hybrid inheritance
# class PremiumAccount(SavingsAccount, SpecialAccount):
#     def premium_benefit(self):
#         print(f"{self.name} enjoys premium benefits!")


# # ------------------- Interactive Banking Menu -------------------
# p = PremiumAccount("Aryan", 1000)

# while True:
#     print("\n--- Premium Account Menu ---")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Add Interest")
#     print("4. Apply Cashback")
#     print("5. Show Premium Benefits")
#     print("6. Show Balance")
#     print("0. Exit")

#     try:
#         choice = int(input("Enter your choice: "))
#     except ValueError:
#         print("Invalid input! Enter a number.")
#         continue

#     match choice:
#         case 1:
#             amount = float(input("Enter amount to deposit: "))
#             p.deposit(amount)
#         case 2:
#             amount = float(input("Enter amount to withdraw: "))
#             p.withdraw(amount)
#         case 3:
#             rate = input("Enter interest rate (default 5%): ")
#             rate = float(rate) if rate else 5
#             p.add_interest(rate)
#         case 4:
#             cashback = float(input("Enter cashback amount: "))
#             p.apply_cashback(cashback)
#         case 5:
#             p.premium_benefit()
#         case 6:
#             print(f"Current balance: {p.balance}")
#         case 0:
#             print("Exiting... Thank you!")
#             break
#         case _:
#             print("Invalid choice! Please select a valid option.")















