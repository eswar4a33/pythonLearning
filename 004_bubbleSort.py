arr=[[5,7,4,1,2,9,6,3,8],[1,0,0,1,0,1,1,1],[1],[],[-1,-4,-7],[-1,-1,-1]]
arr.append(list(range(10,-11,-1)))


def bs(ls):
    for i in range(0,len(ls)):
        for j in range(i+1, len(ls)):
            if ls[i]>ls[j]:
                ls[i],ls[j] = ls[j],ls[i]
    return ls

for x in arr:
    print(bs(x))
