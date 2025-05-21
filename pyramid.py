"""
*   *   *    1
*   *   2    3    4
*   5   6    7    8    9
10  11  12   13   14   15  16



"""
height = int(input("enter the no. lines: "))
x = 1

for i in range(height):
    print("   "*(height-i),end="")
    for j in range(i+1):
        print(x," ",end="")
        x += 1
    for k in range(i):
        print(x," " ,end ="")
        x += 1
    print()
