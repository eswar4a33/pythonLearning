inp = int(input("enter only the odd no. to get a proper diamond \n even if you enter the even no. assumed as number++:"))
def diamond(height):
    hei = height//2+1
    count = 0
    for i in range(1,hei+1):
        i = 2*i - 1
        count += i
    for i in range(hei-1,0,-1):
        i = 2*i -1
        count += i
#    print(count)
    bspace = len(str(count))

    num = 1
    for line in range(1,hei+1):
        print(" "*(hei-line)*(bspace+1), end = "")
        for _ in range(line):
            print(" "*(bspace - len(str(num))),end = "")
            print(num,end = " ")
            num += 1
        for _ in range(line-1):
            print(" "*(bspace - len(str(num))),end = "")
            print(num,end = " ")
            num += 1
        print()
    for line in range(hei-1,0,-1):
        print(" "*(hei-line)*(bspace+1), end = "")
        for _ in range(line):
            print(" "*(bspace - len(str(num))),end = "")
            print(num,end = " ")
            num += 1
        for _ in range(line-1):
            print(" "*(bspace - len(str(num))),end = "")
            print(num,end = " ")
            num += 1
        print()
diamond(inp)
