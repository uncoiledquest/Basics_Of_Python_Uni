def simpleInterest():
    P= float(input("Enter Principal amount: "))
    R= float(input("Enter Rate: "))
    T= float(input("Enter time: "))
    SI=(P*R*T)/100
    print(f"Simple Interest: {SI}")
simpleInterest()