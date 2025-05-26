"""
*   *   *    1
*   *   2    3    4
*   5   6    7    8    9
10  11  12   13   14   15  16
"""

def pyr(height):
    num = 1
    maz = len(str(height*height))

        
    for i in range(1,height+1):
        print(" "*(maz+1)*(height-i),end="")
        for j in range(i):
            print(" "*(maz-len(str(num))),end="")
            print(num,end=" ")
            num += 1
        for k in range(i-1):
            print(" "*(maz-len(str(num))),end ="")
            print(num,end=" ")
            num += 1
        print()
for hei in range(22):
    pyr(hei)


