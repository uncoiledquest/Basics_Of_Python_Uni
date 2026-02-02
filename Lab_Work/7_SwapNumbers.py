a= int(input("Enter a: "))
b= int(input("Enter b: "))

a+=b
b= a-b
a-=b
print(f"Swapped a: {a} Swapped b: {b}")