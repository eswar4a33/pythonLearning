
#2. Check if a number if a number is even/odd. Don't use division or mod(%) operators 
for i in range(0,21,2):
    print(bin(i),end = ",")
for i in range(1,21,2):
    print(bin(i), end = ",")


def evenOddmod(n):
    if n & 1 == 0:
        return "even"
    else:
        return "odd"
for i in range(21):
    print(i,evenOddmod(i))



