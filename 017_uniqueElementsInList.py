"""5. Given a list where some numbers have multiple copies,
return an array where each element had only copy in the original
list e.g [1,2,4,1,3,4,5,6,5] should give [2,3,6]"""


ls = [1,2,4,1,3,4,5,6,5]
lss = []

for i in ls:
    count = 0
    for j in ls:
        if i == j:
            count += 1
            
    if count == 1:
        lss.append(i)    
print(lss)

