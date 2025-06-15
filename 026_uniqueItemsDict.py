# Unique elements in array with dictionary


ls = [1,3,2,2,1,54,6,7,7,8,97,5,0,6,4,7,8,3,5]
dt = {}
for i in ls:
    dt[i] = dt.get(i,0)+1
print(dt)
