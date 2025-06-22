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
        
print()
print(ls)
print()

center = start = end = n//2
print(str(start)+str(end), "-", ls[start][end], end = " ")
while center >= 0:
    i = start
    for j in range(start+1, end+1):
        inx = str(i)+str(j)
        print(inx, "-", ls[i][j], end = " ")
    for i in range(start+1, end+1):
        inx = str(i)+str(j)
        print(inx, "-", ls[i][j], end = " ")
    for j in range(end-1, start-1,-1):
        inx = str(i)+str(j)
        print(inx, "-", ls[i][j], end = " ")
    for i in range(end-1, start-1,-1):
        inx = str(i)+ str(j)
        print(inx, "-", ls[i][j], end = " ")       
    print()
    start -=1
    end +=1
    center -=1




