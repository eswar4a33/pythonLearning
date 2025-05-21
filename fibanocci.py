"""
def fib(n):
    x = []
    if n == 1:
        x = [0]
    elif n == 2:
        x = [0,1]
    elif n > 2:
        x = [0,1]
        while(len(x)<n):
            x.append(x[-1]+x[-2])
    return(x)

n = int(input('enter a value: '))
print(fib(n))

"""


def fib(n):
    x = []
    f = 0
    s = 1
    if n >= 1:
        x.append(f) #[0]
    if n >= 2:
        x.append(s) #[0,1]
    if n > 2:
        while(len(x) < n):
            f = f+s
            x.append(f) #[0,1,1,2]
            f,s = s,f
    
    return x
for i in range(10):
    print(fib(i))

