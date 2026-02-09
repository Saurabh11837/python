# Dictionary Powers
# "mutable" - Dictionaries are mutable, meaning you can change, add, or remove key-value pairs after creation.
# "Duplicates" - Keys must be unique, but you can have duplicates in values.
# "Order" - Dictionary follows insertion order.
# "Heterogenous"- A disctionary can store different types of keys and values. Like integers, strings, lists, or even another dictionary.

# Dictionary syntax and workng 
# Bow we know we have to use key and value pairs to store values in dictionary.
# And the keys in dictionary acts like index values that we use in List

# syntax:
# student={"name":"Saurabh", "age":25}
# print(student["name"])  #Outpue: Saurabh
# print(student["age"])  #Output:25
# print(student)  #Output: {'name': 'Saurabh', 'age': 25}

# # Again telling weww can perform CRUD(create, read update, delete) operations on values but not all on keys cause the keys cannot be changed after creation. 

# # Mutable chek
# student["name"]="Saurabh Patel"
# student.update({"city":"Hazaribagh"})
# print(student)

# # perform CRUD(create, read, update, delte)
# student["mobile"]=7209011155  #create
# student["mobile"]=7209011835  #update
# del student["mobile"]         #deleting
# print(student)                #read


# *****************************************************
# Dictionary traversing
# 1. We can traverse both key and values in dictionary, but default loop is set on keys and you can access the values because of keys..
# 2. So technically you can traverse on both keys and values at the same time.
# *****************************************************
# numbers={1:10, 2:20, 3:30, 4:40, 5:50}

# # this loop acces only kye value
# for i in numbers:  #it this direct loop in list accessing direct value not index, but here direct access key not value
#     print(i)
# # or 
# for i in numbers.keys: #yaha keys likhe or direct access karege to keys hi access hoga value nahi
#     print(i)
# # this loop acces the dictionary key value
# for i in numbers:  
#     print(numbers[i]);
# # or
# for i in numbers.values:   #yaha value likhne se direct value access hota hai 
#     print(i)

# help(dict)   #it help to understand "disctionary" 

# some dicitionary method


#1. "clear" method
# d={1:10, 2:20, 3:30, 4:40, 5:50}
# # d.clear()
# # print(d)

# # 2. "copy" Return a shallow(means not deep copy, agar "means ek list ke data ko koi variable me copy karte hai with 'copy' method then after change in second list data then after not change the fist list ") copy of dict.
# a=[1,2,3,4,5]
# b=a  #This is the method of deeply copy, jab hum b ke koi bhi data change karnge to a ke data change ho jayega
# print(a)
# b[0]=100
# print(a)
# # Shallow copy
# c=a.copy()
# c[0]=1000
# print(c)
# print(a)

# # apply in dictionary
# d={1:10, 2:20, 3:30, 4:40, 5:50}
# e=d.copy()  #apply shallow copye
# e[1]=100
# print(d)

# f=d #apply deep copy
# f[1]=100
# print(d)

# "get" Return the value for key if key is in the dicitionary, else default.
# d={1:10, 2:20, 3:30, 4:40, 5:50}
# e=d.get(2)
# print(e)
# # "items" REturn a set-like object providing a view on the dict's items.
# print(d.items())
# "keys" Return a set like object providing a view on the dict's keys.

# "pop" remove specified key and return the corresponding value.

# "popitem" Remove and return a (key, value) pair as a 2-tuple


# ==========================================================================================
#  Dictionary Questions
# ==========================================================================================
# 1. Write a Python script to merge two Python dictionaries.
# d1={1:10, 2:20, 3:30, 4:40, 5:50}
# d2={6:60, 7:70, 8:80, 9:90, 10:100}

# for i in d2:
#     d1[i] = d2[i]   #update, and create method apply on d1

# print(d1)

# 2. Write a Python program to sum all the value in a dictionary.
# d1={1:10, 2:20, 3:30, 4:40, 5:50}
# sum=0
# for i in d1:
#     sum += d1[i]

# print(sum)
# 3. Count the frequency of each elements in list.
# a=[1,1,1,1,2,2,2,3,4,5,6,6,6,5,1,5,5,1,6,2,1,4,3,5,9,1]

# Simple way
# count=0
# for i in a:
#     if i == 5:
#         count += 1

# print(f"The frequecny of {5} in list {count}")

# using dicitonayr:
# d={}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i]=1
    

# print(d)

# 4. Write a Pythonn program to combine two dictionary by adding value for common keys.
d1={1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
d2={6:60, 7:70, 8:80, 9:90, 10:100}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]   #update, and create method apply on d1
    else:
        d1[i] = d2[i]

print(d1)

