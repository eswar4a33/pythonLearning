def str2int(st):
    res = 0
    for i in st:
        res *= 10
        res += ord(i)-ord('0')
    return res

ls = ['0','1','12','123','1234','12345']   
for i in ls:
    print(str2int(i))

      
