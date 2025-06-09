def fact(n):
    res = 1
    while n>0:
        res = res * n
        n -= 1
    return res
for i in range(10):
    print(i,fact(i))