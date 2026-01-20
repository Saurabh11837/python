# Q1. Accept an interger and Print hello world n times
# Solution

# n=int(input("Enter a numbe to message print n times"))
# for i in range(n):
#     print("Hello Python..") 

# ----------------------------------------------------------------

# ================================================================
# Q2.Print natural up to n.
# Solution...
# n=int(input("Enter a number and print natural number.= "))
# for i in range(1,n+1):print(i)

# ----------------------------------------------------------------
# ================================================================
# Q3.Reverse for loop. Print n to 1.
# Solution...
# n=int(input("Enter a number to print reverse from n to 1 = "))
# for i in range(n,0,-1):
#     print(i)

# ----------------------------------------------------------------
# ================================================================
# Q4.Take a number as input and print it's table
# Solution...
# n=int(input("Enter a number and print table : "))
# for n in range(n,n*10+1,n):
#     print(n)


# ----------------------------------------------------------------
# ================================================================
# Q5.Sum up to n number
# Solution...
# n=int(input("Enter a number and sum 1 to n.. = "))
# sum=0
# for i in range(1,n+1):
#     sum += i

# print(f"Sum of {1} to {n} = {sum}")

# ----------------------------------------------------------------
# ================================================================
# Q6.Factorial of a numebr
# Solution...
# n=int(input("Enter and for find factorial = "))
# fact=n
# factorial=1
# for n in range(n,0,-1):
#     factorial *= n

# print(f"The factorial number of {fact} = {factorial}")

# ----------------------------------------------------------------

# ================================================================
# Q7.Print the sum of all even & odd number in a range separately.
# Solution...
# n=int(input("Enter a number and print sum of all odd and even number = "))
# odd=0
# even=0
# for i in range(1,n+1,1):
#     if(i%2 == 1):
#         odd += i
#     elif(i%2==0):
#         even += i
#     else:
#         continue

# print("Sum of all 'odd' and 'even' nuber..")
# print(f"Odd = {odd}")
# print(f"Even = {even}")



# ----------------------------------------------------------------
# ================================================================
# Q8.Print all the factor of numebr..
# For findign factor of any number we have two method
# 1.Division method:
# 2.Multiplication method:
# 
# 1. Division Method:
# Divide 5 by all integers from 1 up to 5.
# 5 ÷ 1 = 5 → remainder 0 → 1 is a factor
# 5 ÷ 2 = 2.5 → remainder ≠ 0 → not a factor
# 5 ÷ 3 ≈ 1.67 → remainder ≠ 0 → not a factor
# 5 ÷ 4 = 1.25 → remainder ≠ 0 → not a factor
# 5 ÷ 5 = 1 → remainder 0 → 5 is a factor
# ✅ Factors of 5: 1 and 5 

# 2. Multiplication Method:
# Find pairs of numbers whose product is 5.
# 1 × 5 = 5
# 5 × 1 = 5
# ✅ Factors of 5: 1 and 5

# Solution...

# n=int(input("Enter a number : "))
# # 1.Division Rule
# print("Division Rule..")
# for i in range(1,n+1,1):
#     if n%i==0:
#         print(f"{i} is the factor of {n}")
#     continue

# # 2. Multiplication Rule...
# print("Muliplication Rule..")
# for i in range(1,n+1,1):
#     if n%i==0 and i*n/i==n:
#         print(f"{i} is the factor of {n}")
#     continue



# ----------------------------------------------------------------

# ================================================================
# Q9.Accept a number and check if it a perfect number or not.
# A number whose sum of factors is equal to the number itself..

# Example: prefect number 6, 28, 496...
# For n = 6:
# Divisors less than 6: 1, 2, 3
# Sum: 1 + 2 + 3 = 6
# Since sum equals 6, 6 is a perfect number. 
# Solution...
# n=int(input("Enter a prefect number = "))
# prefect = 0
# for i in range(1,n,1):
#     if n%i==0:
#         prefect += i
    
# if n== prefect:
#     print(f"This is  Prefect numebr : {n} == {prefect} ")
# else:
#     print(f"This is Not Prefect numebr : {n} != {prefect} ")

# ----------------------------------------------------------------



# ================================================================
# Q10.Check wether the number is prime or not.
# Solution...
# n=int(input("Enter a number and check it's prime number or not = "))
# if 1==n:
#     print("No, This is odd number but it is not prime number")
# elif n%2==1:
#     print(f"{n} : This is prime number")
# else:
#     print(f"{n} = This is not prime number ")
    

# ----------------------------------------------------------------
# ================================================================
# Q11.Reverse string withoud build function
# Q12.Check string is palindrome or not?
# Solution...
# n=str(input("\nEnter a string data and reverse it = "))
# rev=""
# for i in range(len(n)-1,-1,-1):
#     rev += n[i]

# print(f"\nEnter String : {n}")
# print(f"Reverse String : {rev} \n")

# print("Check string is palindrome  or not")
# if n == rev:
#     print(f"Yes Palindrom : {n} == {rev} \n")
# elif n != rev:
#     print(f"Not Palindrom : {n} == {rev} \n")
# else:
#     print("Not match string \n");


    

# ----------------------------------------------------------------
# ================================================================
# Q13.Count all leters, digits, and special symbols from a given string..?
# Example:
# Given = "P@#yn26at^&i5ve"
# Total count  of chars, digits, and symbols
# Solution...
n="sdf1234561sogn12413@#12$%^&U"

chars=0
digits=0
symbol=0
    
for i in n:
    if i.isalpha():
        chars += 1
    elif i.isdigit():
        digits += 1
    else:
        symbol += 1

print(f"Chars : {chars}")
print(f"Digits : {digits}")
print(f"Symbol : {symbol}")
# ----------------------------------------------------------------


# Day 1 practice completed
