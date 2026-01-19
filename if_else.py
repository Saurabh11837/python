# This is a simple if-else statement in Python
# What is if else?
# The if-else statement is a conditional statement that allows you to execute certain blocks of code.
# based on whether a specified condition is true or false.
# Syntax:
# if condition:
#     # code to be executed if the condition is true
# else:
#     # code to be executed if the condition is false

# Example: only if condition, its check the condition is true or false
# x = 10
# if x > 5:
#     print("x is greater than 5");

# # Example: if-else condition
# y = 3
# if y > 5:
#     print("y is greater than 5");
# else:
#     print("y is not greater than 5");

# Example: if-elif-else condition
# z = 15
# if z < 10:
#     print("z is less than 10");
# elif z < 20:
#     print("z is between 10 and 20");
# else:
#     print("z is 20 or greater");
 
# Example: nested if-else condition
# a = 8
# if a > 5:
#     if a < 10:
#         print("a is between 5 and 10");
#     else:
#         print("a is 10 or greater");
# else:
#     print("a is 5 or less");

# Pracrice example
# money = int(input("Enter the amount of money you have: "))
# if money >= 10:
#     print("You can buy a Choko bar.")
# elif money >= 20:
#     print("You cannot buy a mongo ice. ")
# else:
#     print("You cannot buy anything.")


# Pracitce quection
# Q1. Accept two numbers and print the greatest number between them.
# print("Enter Two number :")
# number1 = int(input("Enter first number  : "))
# number2 = int(input("Enter second number  : "))

# if number1 == number2:
#     print(f"Both number is equal : {number1} == {number2}");
# elif number1 > number2:
#     print(f"First number is greather than second number {number1} > {number2}");
# elif number1 < number2:
#     print(f"Second number is greather than first number {number1} < {number2}");
# else:
#     print("Some isuu in program please enter valid numebr ")

# Q2. Accept the gender from the user as char and print the respective greeting message
# Eg, Good Morning Sir(on the basis of gender)

# gender = str(input("Enter your genter \n 'male' or 'female'.. "))

# if gender == "male" or gender== "MALE":
#     print("Good Morning Sir");
# elif gender == "female" or gender == "FEMALE":
#     print("Good Morning mam ")
# else:
#     print("Unidentified gender..")


# Q3. Accept an inter and check whether it is an even number or odd.
# number=int(input("Enter a number to check even or odd : "))
# if number%2==0:
#     print(f"This number {number} is even... ")
# elif number%2==1:
#     print(f"This number {number} is odd...")
# else :
#     print("Some issu in input...")

# Q4. Accept name and age from the user. Check if the user is a valid voter or not.
# Eg:- "hello shery you are a valid voter "
# print("Enter your name and age for verify for you a valid voter or not..");
# name=str(input("Name : "))
# age=float(input("Enter your age : "))
# if age>= 18:
#     print(f"Hello {name} you are a valid voter")
# else:
#     print(f"Hello {name} you are not valid voter or not adult...")

# Q5. Accept a year and check if it a leap year or not?
# year= int(input("Enter any year and check this is leap year or not = "))
# if year%100==0 and year%400==0:
#     print(f"{year} This is leap year..")
# elif year%100 != 0 and year %4 ==0:
#     print("It's a leap year...")
# else:
#     print(f"{year} This is not leap year..")

# Q6. use if and elif using multiple condition of elif
# take the input of temprature in celsius.
# 1. Below 0 degree --> "Freezubg cold"
# 2. 0 degree to 10 degree celsius -> "Very cold"
# 3. 10 degree to 20 degree celsius-> "Cold"
# 4. 20 degree to 30 degree celsius-> "Pleasant"
# 5. 30 degree to 40 degree celsius-> "Hot"
# 5. 40 degree to 50 degree celsius-> "Very Hot"

celsius=int(input("Enter number of temprature to claculate the enviroremnt detail.. = "))
if celsius <= 0:
    print("Freeezing cold")
elif 0 < celsius and celsius <= 10:
    print("Very Cold")
elif 10 < celsius and celsius <= 20:
    print(" Cold")
elif 20 < celsius and celsius <= 30:
    print("Pleasant")
elif 30 < celsius and celsius <= 40:
    print("Pleasant")
else:
    print("Very Hot")






