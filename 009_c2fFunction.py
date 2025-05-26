
"""
import math
a = 10
b = 10
print(math.sqrt(pow(a,2)+pow(a,2)))


"""

def add(a,b,c):
    print(a,b,c)
    r = a+b+c
    a = 5
    b = 6
    c = 7
    print(a,b,c)
    return a,b,c

a = 10
b = 20
c = 30
print(a,b,c)
e,f,g = add(a,b,c)
a,b,c = add(a,b,c)

print(e,f,g)
print(a,b,c)

