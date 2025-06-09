def fib(n):
    f = 0
    s = 1
    for i in range(n):
        f ,s = f + s, f

    return f
for i in range(1, 8):
    print(i, fib(i))