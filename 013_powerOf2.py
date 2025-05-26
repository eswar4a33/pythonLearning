#1. Check if a number is power of 2 or not (e.g 2,4,8,16...256, 1024, 4096)


def power2(n):
    while n:
        rem = n%2
        quo = n//2
        if rem == 1:
            return False
        else:
            if quo == 1:
                return True
        n = quo

for i in range(1,20):
    print(i, power2(i))
for i in range(5,15):
    print((2**i)-1,power2((2**i)-1))
    print((2**i),power2((2**i)))
    print((2**i)+1,power2((2**i)+1))
    
