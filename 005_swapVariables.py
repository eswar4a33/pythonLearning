def swapWithTemp(a,b):
    temp = a
    a = b
    b = temp
    return a,b
def swapPython(a,b):
    a,b = b,a
    return a,b
def swapWithFunction(a,b):
    return b,a
def swapXOR(a,b): # a = 5(101) , b = 7(111)
    a ^= b # a = a ^ b (101 ^ 111)  010(2)
    b ^= a # b = b ^ a (111 ^ 010)  101(5)
    a ^= b # a = a ^ b (010 ^ 101)  111(7)
    return a,b # a = 7(111), b = 5(101)
def swapAddition(a,b):
    a = (a + b)
    b = a - b
    a = a - b
    return a,b

def swapSubtraction(a,b):
    b = b - a
    a = a + b
    b = a - b
    return a,b

def swapMultiplication(a,b):
    a = a * b
    b = a // b
    a = a // b
    return a,b

def swapDivision(a,b):
    a = b / a
    b = b / a
    a = a * b
    return int(a),int(b)

a = 5
b = 7
print(swapWithTemp(a,b))
print(swapPython(a,b))
print(swapWithFunction(a,b))
print(swapXOR(a,b))
print(swapAddition(a,b))
print(swapSubtraction(a,b))
print(swapMultiplication(a,b))
print(swapDivision(a,b))
