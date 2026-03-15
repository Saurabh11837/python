# List powers.
# Before starting we need to understand some of the terminology.
#   --> Mutabble - Mutability refers to whether an object's value can be changed after creation. And List allow this.
#   --> Duplicates - we know data structures are used to store multiple values so duplicates means same value occuring multiple time. List allows this.
#   --> Ordered - List maintains ordered data structure maintains the sequence of elements as they were inserted. This means you can access elements using their position(index).
#   --> Heterogenous - List have heterogenous nature that means we can have multiple data types inside the list.
# Heterogenous example : a=[12,13,14, 15.5, True, print(), "raj"]
# List Basics
# First we have to know what is the syntax of list and how, to create a list we have to use squrare brackets([]).
# Example : fruits = ["apple","banana","cherry"]
#           numbers =[10, 20, 30, 40]

# This is the example of Hetrogenous list
a=[12,13,14, 15.5, True, print("Sauravvvv"), "raj"]  

# 1st way to accessing list value using index
# for i in range(0,len(a),1):  
#     print(a[i])


# 2nd way directly on values
# for i in a:
#     print(i)


# # slice list data
# b=a[0:5]
# print(b)


# dir() is a built-in function in Python that, when called with an object (like list), returns a list of all the methods and properties available for that object.

# list is a built-in class in Python, and when passed to dir(), it shows the available functions and properties that can be used with lists, such as append(), remove(), extend(), etc.
# print(dir(list))

# OUTPUT
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# ===========================================================
# append method example
# ===========================================================

# # Create a list
# my_list=[1,2,3]
# print(my_list)

# # Append a number to the list
# my_list.append(4)

# # Append a String to the list
# my_list.append("hello")

# # Output the list after appending elements
# print(my_list)

# # declear a new list and add in fist list
# one_list=[5,6,7]
# my_list.append(one_list)
# # add all new list data in first list using looping index
# for i in range(0,len(one_list),1):
#     my_list.append(one_list[i])

# two_list=[8,9]
# for i in two_list:
#     my_list.append(i)
    

# print(my_list)


# ===========================================================
# insert method example
# ===========================================================

# Syntax:  list.index(index, element)

# index: The position where you want to insert the element. The index is 0-based (i.e., the first position in the list is 0).

# element: The item that you want to insert into the list.

# my_list=[1,3,4,6]
# print(my_list)

# # Insert 4 at index of 1 (index start form 0 so second index stroing data usin 1).
# my_list.insert(1,4)
# my_list.insert(5,5)
# # Output the the list after inserting the element
# print(my_list)

# # Create a list of strings
# fruits = ['apple', 'banana', 'orange']

# # Insert 'grape' at index 1
# fruits.insert(1, 'grape')

# # Output the list after inserting
# print(fruits)

# If the index is greater than the length of the list, the element is appended at the end.

# If the index is negative, it counts from the end of the list (e.g., -1 is the last position, -2 is second from last, etc.).


# How to insert multiple in list
# 1. Using Slicing
# 2. Using a Loop
# 3. Using extend() method, if data adding at the end.

# Slicing Syntax
# sequence[start:stop:step]
# start: The index where slicing begins (inclusive). Defaults to 0.
# stop: The index where slicing ends (exclusive); it stops just before this position.
# step: (Optional) The interval between indices. Defaults to 1


# print("Insert multipal data using slicing method")
# one_list=[1,5,8]
# print(one_list)

# # Insert multiple elements at index 2
# one_list[1:1]=[2,3,4]
# print(one_list)
# one_list[5:5]=[6,7]
# print(one_list)

# # 2. Using a loop
# print("Insert multiple data in list using a loop..")
# two_list=[1,5,8]
# print(two_list)
# element_to_insert1=[2,3,4]
# # Insert multiple elements at index 2
# for elem in reversed(element_to_insert1):
#     two_list.insert(1,elem)

# element_to_insert2=[6,7]
# for elem in reversed(element_to_insert2):
#     two_list.insert(5,elem)

# print(two_list)

# ===========================================================
# extend method example
# If you simply want to add multiple elements at the end of the list, then you can use extend():
# ===========================================================

# 3. Using extend(), method
# print("Using extend method add multiple data end of the list")
# three_list=[1,2,3]
# print(three_list)
# three_list.extend([4,5,6,7,8])
# print(three_list)

# ===========================================================
# remove method example
# ===========================================================

# In Python, the remove() method is used to remove the first occurrence of a specified element from a list. If the element is not found, it raises a ValueError.
# Syntax:
# list.remove(element)
# Create a list
# my_list = [1, 2, 3, 4, 2, 5]
# num= int (input("Enter a number which you want to remove in the list : "))
# # Remove the first occurrence of 2
# try:
#     # Try to remove an element that does not exist
#     my_list.remove(num)
# except ValueError:
#     print("Element not found!")

# # Output the list after removing the element
# print(my_list)


# ===========================================================
# Practice list question
# ===========================================================

# 1. find positive and negative number in the list
# list_Data=[45,-9,6,8,-8,8,8,-5,45,5,6]
# print("Positive element are : ")
# for i in list_Data:
#     if(i>=0):
#         print(i)
# print("Negative element are : ")
# for i in list_Data:
#     if(i<=0):
#         print(i)

# 2.Find the Mean of the list elements.
# mean=sum of all list element and divide total number of element.
# list_Data=[5,2,3,6,4]
# sum=0
# for i in range(0,len(list_Data),1):
#     sum += list_Data[i]

# print(f"Sum of all list data is : {sum}")
# print(f"Total num of element = {len(list_Data)}")
# mean=sum/len(list_Data)
# print(f"The mean of list data is : {mean}")


# 3.Find the greatest element and print its index too.
# list_Data=[5,2,3,6,4]
# # Initialize greatest and smallest with appropriate values
# greatest=float('-inf') #Smallest posssible number
# smallest=float('inf')  #Largest Possible integer number
# print(f"Greatest : {greatest} \n Smallest : {smallest}")

# for i in range(0,len(list_Data),1):
#     if(greatest<list_Data[i]):
#         greatest=list_Data[i]
#     if(smallest>list_Data[i]):
#         smallest=list_Data[i]
# print(f"The greatest number is : {greatest}")
# print(f"The Smallest number is : {smallest}")

# 4.Find the second greatest and smallest number in the list
# list_Data=[5,2,3,6,4,1,9,8,7]
# print(list_Data)
# # Initialize greatest and smallest with appropriate values
# greatest=float('-inf') #Smallest posssible number
# smallest=float('inf')  #Largest Possible integer number
# print(f"Greatest : {greatest} \n Smallest : {smallest}")

# for i in range(0,len(list_Data),1):
#     if(greatest<list_Data[i]):
#         greatest=list_Data[i]
#     if(smallest>list_Data[i]):
#         smallest=list_Data[i]
# print(f"The greatest number is : {greatest}")
# print(f"The Smallest number is : {smallest}")

# list_Data.remove(greatest)
# list_Data.remove(smallest)
# print(f"List after removing greatest and smallest : {list_Data}" )
# second_greatest=float('-inf')
# second_smallest=float('inf')
# for i in range(0,len(list_Data),1):
#     if(second_greatest<list_Data[i]):
#         second_greatest=list_Data[i]
#     if(second_smallest>list_Data[i]):
#         second_smallest=list_Data[i]

# print(f"The Second Greatest number is : {second_greatest}")
# print(f"The Second Smallest number is : {second_smallest}")

# Find second greatest and smallest number using shorting method
# list_Data=[5,2,3,6,4,1,9,8,7]
# print(f"Original list : {list_Data}")

# # Sort the list
# sorted_list = sorted(list_Data)

# second_smallest = sorted_list[1]
# second_greatest = sorted_list[-2]
# print(f"The second greatest number is: {second_greatest}")
# print(f"The second smallest number is: {second_smallest}")


# Alternative Approach Without sorting
# list_Data = [5, 2, 3, 6, 4, 1, 9, 8, 7]
# print(f"Original list: {list_Data}")

# # Initialize values
# greatest = float('-inf')
# second_greatest = float('-inf')
# smallest = float('inf')
# second_smallest = float('inf')

# for num in list_Data:
#     if num>greatest:
#         second_greatest=greatest
#         greatest=num
#     elif num>second_greatest and num!=greatest:
#         second_greatest=num

#     if num<smallest:
#         second_smallest=smallest
#         smallest=num
#     elif num<second_smallest and num!=smallest:
#         second_smallest=num

# print(f"The greatest number is : {greatest} \nsecond greatest number is : {second_greatest}")
# print(f"The smallest number is : {smallest} \nsecond smallest number is : {second_smallest}")

# 5.Check if list is shorted or not
# first_list = [1, 2, 3, 4, 5]
# second_list = [1, 5, 4, 2, 3]

# if first_list == sorted(first_list):
#     print("First list is sorted in ascending order.")
# else:
#     print("First list is not sorted")
# if second_list == sorted(second_list):
#     print("Second list is sorted in ascending order.")
# else:
#     print("Second list is not sorted")
