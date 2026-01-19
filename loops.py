# # Loops
# # what is loops in python
# # Loops are used to execute a block of code repeatedly until a certain condition is met.
# # Python provides two types of loops: for loops and while loops.
# # 1. For Loop
# # A for loop is used to iterate over a sequence (like a list, tuple, dictionary)
# # or other iterable objects. It allows you to execute a block of code for each item in the sequence.
# # Syntax:
# # for item in sequence:
# #     # code to be executed for each item   


# # what is range() function
# # The range() function generates a sequence of numbers, which is commonly used in for loops.
# # Syntax:
# # range(start, stop, step)

# # Example:
# x = range(1,10,1)
# for i in x:
#     print(i)
# # Output: 0 1 2 3 4 5 6 7 8 9
# # Example:
# y=range(1, 10, 2)
# for i in y:
#     print(i)
# # Output: 1 3 5 7 9

# # Example:
# y=range(1, 10, 3)
# for i in y:
#     print(i)
# # Output: 1 4 7

# # Example:
# y=range(2, 10, 2)
# for i in y:
#     print(i)
# # Output: 2 4 6 8
# # Example:
# y=range(2, 10, 3)
# for i in y:
#     print(i)
# # Output: 2 5 8

# # Example
# for i in range(1,21,1):
#     print(1)

# for i in range(10):  # if we not set the start index and step it set by defautl 1
#     print(i)

# print the number 1 to 10 with revere order
# for i in range(10,0,-1):
#     print(i)


# for i in range(-3,-16,-1):
#     print(i)

# ============= lets print a table of 5 ==============
# n = int(input("Which table you want to print ? "))
# for i in range(n,n*10+1,n):
#     print(i)


# ==============================
# Loops to stirngs
# ==============================
# Loops for striings work slightly differently, You can iterate through a string in two ways:
# 1. Using index values.
# 2. Iterating directly overt the string

# Example 1: Iterating using the index values, Now we know that index values are numbers and for numbers we again have to use range function.
# Here you iterated over the string using the index values for better understanding watch the video.
a="Nature"
# for i in range(6):
#     print(a[i])
# for i in range(len(a)):
#     print(a[i])

# Example 2: Second way is simple we cna directly iterate but using this method will give you the direct access to the characters instead of index values.
b="Nature"
# for i in a:
#     print(i)


# Using break keyword
print("Using break keyword...")
for i in range(1,10):
    if i==5:
        break
    else:
        print(i)
# using contine keyword
print("Using Continue keyword...")
for i in range(1,10):
    if i==5:
        continue
    else:
        print(i)
for i in range(1,10):
    if i==5:
        continue
    print(i)