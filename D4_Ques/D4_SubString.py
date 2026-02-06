""" 
Create a Python program that accepts a string and a substring from the user.
The program should count the total number of occurrences of the substring within the string and print the result.

 """

x=input("Enter a String: ")
x.upper()
y=input("Enter SubString you want to check: ")
y.upper()
yLen=len(y)
count=0
for i in range(0,len(x)):
    if x[i:i+yLen] == y:
        count+=1

print(f"Number of Occurence: {count}")