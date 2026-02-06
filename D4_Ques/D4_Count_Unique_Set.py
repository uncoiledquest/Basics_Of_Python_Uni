""" 
Create a Python program that takes a string as input and prints the number of times each character appears in the string.

 """

x=input("Enter a String: ")
Count= {}
for i in x:
    if x.isalpha():
        Count[i]=Count.get(i,0)+1

for i in Count:
    print(f"{i} : {Count[i]}")