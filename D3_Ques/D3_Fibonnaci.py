"""
Finding Fibonacci Series using Iteration and Recursion.

"""

x=int(input("Enter number till which you want the Fibonnaci series: "))

#Iteration

"""
a,b=0,1
while a<x:
    print(a, end=" ")
    a,b=b,a+b 
    
"""

#Recursion

def fib_upto(n, a=0, b=1):
    if a > n:
        return
    print(a, end=" ")
    fib_upto(n, b, a + b)

fib_upto(x)
