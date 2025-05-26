"""5. Given a list where some numbers have multiple copies,
return an array where each element had only copy in the original
list e.g [1,2,4,1,3,4,5,6,5] should give [2,3,6]"""


ls = [1,2,4,1,3,4,5,6,5]
lss = []

for _ in range(len(ls)):
    x = ls.pop(0)
    if x not in ls:
        lss.append(x)
print(lss)

