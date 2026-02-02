x= int(input("Enter Starting range: "))
y= int(input("Enter Ending Range: "))

print("\nEven Number: ")
for i in range(x,y+1):
    if i%2==0:
        print(f"{i}, ", end="")

print("\n\nOdd Number: ")
for i in range(x,y):
    if i%2!=0:
        print(f"{i}, ", end="")