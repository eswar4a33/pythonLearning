take = int(input("enter a number:"))

for i in range(1, take+1):
    res = ""
    if i % 3 == 0:
        res = "honey"
    if i % 5 == 0:
        res += "bunny"
    if not res:
        res = i
    print(res)
    
