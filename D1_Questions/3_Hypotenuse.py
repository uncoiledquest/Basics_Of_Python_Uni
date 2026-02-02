import math

perpendicular= float(input("Enter base of a Right-Angled Triangle: "))
base= float(input("Enter Perpendicular of a Right-Angled Triangle: "))

c= math.hypot(perpendicular,base)
"""
OR

c= math.sqrt(perpendicular**2+base**2)


"""
print(f"Hypotenuse of the given triangle is: {c}")