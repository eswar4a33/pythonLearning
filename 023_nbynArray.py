n = int(input('enter a number: '))
ls = []
ls1 = []
for i in range(1,n*n+1):

    print(f"{i:2}",end = " ")
    ls1.append(i)
    if i % n == 0:
        print()
        ls.append(ls1)
        ls1 = []

for i in range(len(ls)):
    print(ls[i])