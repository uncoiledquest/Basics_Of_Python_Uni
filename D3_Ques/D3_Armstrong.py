
#To find whether a Number is Armstrong or Not. 

x=int(input("Enter a number: "))
temp=x
sum=0
dig=0

while temp>0:
    temp=temp//10
    dig+=1

temp=x
while temp>0:
    sum+=(temp%10)**dig
    temp=temp//10

print("Number is Armstrong." if sum==x else "Number is not Armstrong")