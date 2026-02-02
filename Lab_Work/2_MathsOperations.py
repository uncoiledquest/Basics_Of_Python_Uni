a= float(input("Enter integer a: "))
b= float(input("Enter integer b: "))
add= a+b
sub= a-b
mul= a*b
div= False
mod= False
if b==0:
    print("Divisor Can't be 0!")
else: 
    div=a/b
if b==0:
    print("Divisor Can't be 0!")
else: 
    mod=a%b
print(f"Additon: {add}\nSubtraction: {sub}\nMultiplication: {mul}\nDivision: {div}\nModulus: {mod}")

