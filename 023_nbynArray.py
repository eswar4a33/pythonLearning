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

center = start = end = n//2
l = []
while center >= 0:
    for i in range(start, end+1):
        for j in range(start, end+1):
            inx = str(i)+str(j)
            if inx not in l:
                l.append(inx)
                print(i,j,end = " ")
        
    print()
    start -= 1
    end += 1
    center -= 1




