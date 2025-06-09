def fib(f, s, n):
    if n<1:
        return s
    return fib(f+s,f,n-1)

for i in range(1,10):
    f = 0
    s = 1
    print(i,fib(f,s,i))