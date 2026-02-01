# Tuple
# Before starting we need to understand some of the terminology
# 1. Immutable : Tuples are not mutable you cannot change the values of tuple 
# 2. Duplicates : You can have duplicate values in tuple there are no restriction.
# 3. Ordered : Set are ordered and you can access them through index values.
# 4. Heterogenoues : Set also have heterogenous nature and can have different types of data structure in tupel

# Tuple traversing and methods
# --> Tuples asre traversed in the same manner as List are traversed.
# --> But remember tuples are like strings you can't change anything once it's mdade we can't change them.
# --> Well the use case is not much in question solving but still you have to understand it.
# --> Method of tupel are:
#   1. index, 2. count
# Yes there are only 2 methods of tuple one for finding the index and othre of countng the occurrences of an element.


# # Heterogenouees: means sotre multiple different type of values
# b=(1,2,2,3,3,2,2.5,3.6,"Saurabh","a",print(),True)

# a= (1,2,2,3,4,5,6)
# print(a)
# print(type(a))
# # Access through index 
# print("Accessing tuple data with indexing")
# print(a[0])
# print(a[1])
# print(a[2])

# # Accessing direct way
# print("Accessing through loops in direct way")
# for i in a:
#     print(i)

# # Accessing through index
# print("Accessing through loop with indxing ")
# for i in range(0,len(b),1):
#     print(b[i])

# # Method uses on tuple
# c=(5,2,9,1,5,6,5,5,5)
# index=c.index(9)
# count = c.count(5)
# print(f"Index: {index} \nCount : {count}, \nLenght : {len(c)} ")


# tuple unpacking (we also konwn as destructuring)

a,b,c,d=(1,2,3,4)
print(a,b,c,d)

d=(1) # Output Here python compiler treated as a integer becaue in braces only one value and here also tuple unpacking
print(type(d)) 
d=(1,) # Output Here python compiler treated as a tuple becauer in braces only one value but after one value one commo so here treated next is the value so compiler treated as a tuple
print(type(d)) 