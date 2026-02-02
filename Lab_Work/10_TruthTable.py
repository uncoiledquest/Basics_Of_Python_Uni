print(" AND & OPERATOR: \n x | y | z\n----------")
for x in range(0,2):
    for y in range(0,2):
        z= x&y
        print(f" {x} | {y} | {z}")

print("\n\nOR | OPERATOR: \n x | y | z\n----------")
for x in range(0,2):
    for y in range(0,2):
        z= x|y
        print(f" {x} | {y} | {z}")
        
print("\n\nXOR^ OPERATOR: \n x | y | z\n----------")
for x in range(0,2):
    for y in range(0,2):
        z= x^y
        print(f" {x} | {y} | {z}")
