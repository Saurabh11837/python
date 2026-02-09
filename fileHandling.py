# File Handling

# What is files?
# 1. You all know what are files any name with an extension is file.
# 2.Now that extension can be .py, .txt, .mp3 etc. and when we want to handle these files we use file handling.

# File Handling
# 1.File handling means Creating, Reading, Updating, Deleting(CRUD) operations that we can perform in files.
# 2.Now lets see how to perform these operations in python.
# 3.We have to use open() function to open a file in python.

# ****************************************************************************************************************
# Now there are multiple modes to open the file.

#   Mode         Description
#   'r'     -> Read(default)-file must extist.
#   'w'     -> Write - creates files or overWrites.
#   'a'     -> Append- adds to end of file
#   'x'     -> Create - creates a new file fails if it exists.

# ****************************************************************************************************************







# p=open(r'H:\javaLeetCode/array1.java')

# print(p.read())   

# OUTPUT:
# PS D:\python> python fileHandling.py

# Given an array of integers nums and an integer target, return indices of the two numbers such
# that they add up to target.You may assume that each input would have exactly one solution,
# and you may not use the same element twice. You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
# */

# import java.util.Scanner;
# class Solution {
#    /* public static int[] twoSum(int[] nums, int target) {
#         int count=0;
#         int arr[]=new int[2];
#         for(int i=0;i<nums.length;i++){
#             for(int j=i+1;j<nums.length;j++){
#                 if(nums[i]+nums[j]==target){
#                     arr[count++]=i;
#                     arr[count]=j;
#                     return arr;
#                 }
#             }
#         }
#         return arr;
#     }*/
#         public static int[] twoSum(int[] nums, int target) {
#         int n = nums.length;
#         for (int i = 0; i < n - 1; i++) {
#             for (int j = i + 1; j < n; j++) {
#                 if (nums[i] + nums[j] == target) {       
#                     return new int[]{i, j}; //Solution found and return
#                 }
#             }
#         }
#         return new int[]{}; // No solution found
#     }
#     public static void main (String args[]){
#         Scanner s=new Scanner(System.in);
#         int n=s.nextInt();
#         int nums[]=new int[n];
#         int target=s.nextInt();
#         int newarr[]=twoSum(nums,target);
#                 for(int i=0;i<=newarr.length;i++){       
#                         System.out.println(newarr[i]);   
#                 }
#     }
# }
# PS D:\python>
# 

write=open("superman.txt",'w')
append=open("superman.txt",'a')

write.write("Hello this is akarsh and I am writing inside this file ")
append.write("I am somethign append in this file..")
write.close()

create=open("Hii.txt",'x') #it create only new file

