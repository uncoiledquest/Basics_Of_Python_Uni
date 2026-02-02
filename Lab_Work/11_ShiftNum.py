x= int(input("Enter a Number: "))
xb= bin(x)[2:]
ch= int(input("Enter Right or Left Shift(1/2): "))
shift= int(input("Enter how much places Shift: "))
if ch==1:
    y= x>>shift
    yb= bin(x)[2:]
elif ch==2:
    y= x<<shift
    yb= bin(y)[2:]


print(f"\nGiven Number: {x}\nBinary Representation of Given Number: {xb}")
print(f"\n\nBinary Representation of Shifted Number: {yb}\nValue of Shifted Number in Decimal: {y}")
