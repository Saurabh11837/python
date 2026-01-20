# While loops 
# --> The while loop repeats a block of code as long as aa condition is True. It is useful when the number of iteration is unknown before execution.
# Syntax
# while condition:
#       Code to execute
# 
# Example:
# a=1
# while a<= 10:
#     print(a)
#     a += 1

# While loop practice qeustions
# Q1. Separate each digit of a number and print it on the new line.
# print(10 / 3)   # Normal Devison, 3.3333333333333335
# print(10 // 3)  # Floor Divions(Ye sirf integer result deta hai), 3

# Separate means 
# 2
# 5
# 6
# a=int (input("Tell your number : "))
# while a > 0:
#     print(a%10)
#     a=a//10

# Q2. Accept a number and print its reverse.
# a=int (input("Tell your number : "))
# reverse=0
# while a>0:
#     reverse=(reverse*10)+a%10
#     a=a//10

# print(f"The rever numer : {reverse}")


# Q3. Accept a numer and check if it is a palindromic number(if number and its reverse are equal);
# a=int (input("Tell your number : "))
# user=a
# reverse=0
# while a>0:
#     reverse=(reverse*10)+a%10
#     a=a//10

# if user == reverse:
#     print(f"This is palindromic number: {user} == {reverse}")
# else:
#     print(f"This is Not palindromic number: {user} != {reverse}")

# Q3. Create a random number guessing game with python.
# Here random is library
import random

num=random.randint(1,100)
print(f"Random number {num} ")
tries=0

while True:
    guess=int(input("Please guess your number 1 to 100 :- "))
    if num == guess:
        tries += 1
        print(f"Your are right guess the number is {tries} tries")
        break
    elif num<guess:
        tries +=1
        print("Go a litter lower")
    elif num>guess:
        print("Go a littel higher")
        tries +=1
    else:
        tries +=1
        print("Sorry you are wrong")    




