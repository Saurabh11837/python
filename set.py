# Set in Python

# Before starting the "set", we need to understand some of the terminology.
# 1. mutable : Sets are mutable you can change the values of set.
# 2. NoDuplicates : You cannot have any duplicate values in set that means every element will be unique.
# 3. Unordered : Sets are unordered and you cannot access them though index values.
# 4. Hetrogenous : Set is semi-hetrogenous it can store some data types like string, numbers, tuples but not everything.

# How Set stores value in python
# 1. Each value in a set is hashed using a hash function (hash() in Python).
# 2. The hash is used as an index to store the element in memory.
# 3. Since hashing does not maintin order, sets are unordered.
# 4. Only immutable (hashable) objecccts can be stored in a set. (e.g., numbers, strings, tuples). Mutable objects like lists and dicitionaries are not allowed.


# Syntax of set(mutable, NoDuplicate value(if you inset duplicate value set is ignored), Unordered (not access through index) ). 
# variableName = {storingdata, data, 12,};

# Example
# s={1,2,3,4,5,5,6}

# print(s); 

# if you are accessing through index of set data compiler will throw the error, because set stored value in hashed way.
# print(s[1]) 

# Stored hash value of some string
# a=hash("hello")
# print(a) #Output = 1687015576017001992, (ye jo "hello" ka hash value hai humes same nahi rahega kyuki string ke hash value humesh change hote rahta hai DOS Attack ke kaaran in python after 3.3 version)

# Stored hash value of tuple, but every time output is same because integer ka hash value change nahi hota cahe wo normal ho ya tuple ke andar ho ya list ke  andar ho
# b=hash((1,2,3,4))
# print(b)  #iska hash value change nahi hoga everry run pe same hi rahega.

# store in tupe hetrogenous type data, and show the output of tuple.
# print(hash((1,2,"abc",3,4)))
# print(hash((1,2,"abc",3,4)))


# Access set data through loop as a direct ways not through index because index does not exist in index, set store data in hash way.
# iska output humesha shorting me rahata hai 
# a={3,5,1,4,2}
# for i in a:
#     print(i)

# Output here ever time output is same because in set stored data only integer and integer hex value not change every time.
# 1
# 2
# 3
# 4
# 5

# if in set store in one of single data is string then the output is change
# Example: isme jab bhi output print hoga ordered same nahi hoga kabhi string first me, to kabhi last ya middle me hoga 
# b={1,2,3,"hello",4}
# for i in b:
#     print(i)



# ****************************************************************************************************
# Set Traversing 
# 1. A set cannot be traversed using the index values cause it is unordered and has no index.
# 2. So many times it will give random values. you can watch the video for complete understanding.

# Set methods
# 1. Now set methods are very powerful cause you don't have any indexing you cannot change the values but set is mutuble so we use methods for this.
# 2. For adding and revoving the elements you can use methods as follows.

# Example:
# s={1,2,3}
# print(s)

# s.add(4)  # Adds an element to the set
# print(s)
# s.remove(2) # Remove 2 (Raises an error if not found).
# print(s)
# s.discard(5)  #Remove 5 (No error if not found)
# print(s)
# popped_element = s.pop( )  #Remove a random element and stored it. and ye humesha smallest element ko delte karega
# print(s)
# s.clear() #Removes all elements
# print(s)


# ****************************************************************************************************



# ************************************************************************************************************
# Some method apply on two set
# Exaple:
# A = {1,2,3}
# B = {3,4,5}
# union_set = A.union(B)  # Output : {1,2,3,4,5}
# intersection_set = A.intersection(B) #Output: {3} ,In shortcut way, c= A&B
# difference_set1 =  A-B #Output: {1,2}, this is the shortcut way find the difference
# difference_set2 =  B-A #Output: {4,5}, this is the shortcut way find the difference

# symmetric_diff = A.symmetric_difference(B) #Output: {1,2,4,5}

# print(f"Set B : {A}")
# print(f"Set B : {B}")

# print(f"Union set of A & B : {A | B}")  #This the shortcut method for find the Union, OUTPUT: {1,2,3,4,5}
# print(f"Intersection of A & B : {A & B}")  #This the shortcut method for find the Intersection  OUTPUT: {3}
# print(f"Difference of A from B : {A - B}")  #This the shortcut method for find the Difference  OUTPUT: {1,2}
# print(f"Difference of B from A : {B - A}")  #This the shortcut method for find the Difference OUTPUT: {4,5}
# print(f"Symmetric difference of A & B : {A ^ B}")  #This the shortcut method for find the Symmetric Difference OUTPUT: {1,2,4,5}


# print(f"Union set of A & B : {union_set}")
# print(f"Intersection of A & B : {intersection_set}")
# print(f"Difference of A from B : {difference_set1}")
# print(f"Difference of B from A : {difference_set2}")
# print(f"Symmetric difference of A & B : {symmetric_diff}")

# Usint through compund operator
# example: of compund operator 
# a = 5;
# a += 10
# print(a) #outpue : 15

# this compund using in the math section

a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a)
print(b)
a |= b  #a union b Outpue: {1,2,3,4,5,6,7,8}

print(a) 

 




# ************************************************************************************************************