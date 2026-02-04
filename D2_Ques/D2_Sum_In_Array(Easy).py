""" 
LEET CODE QUESTION.

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1] 
"""
num=int(input("Enter number of elements you want in the array: "))
arr=[]
print("Enter elements: ")
for i in range(0,num):
    arr.append(int(input()))
sum= int(input("Enter the sum you want: "))
k=0
l=0
flag=0

for i in range(0,num):
    for j in range(i+1,num):
        if arr[i]+arr[j]==sum:
            k=i
            l=j
            flag=1
            break
if flag==0:
    print("No such sum was found")
else:
    print(f"Indices: [{k},{l}]")
