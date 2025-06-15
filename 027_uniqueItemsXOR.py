#Find the only Unique element in an array with XOR


ls = [1,3,2,2,1,54,6,7,7,8,97,5,0,6,4,7,8,3,5]
ls1 = []

for i in ls:
    count = 0
    for j in ls:
        if i ^ j == 0:
            count += 1
    if count == 1:
        ls1.append(i)
print(ls1)
            
