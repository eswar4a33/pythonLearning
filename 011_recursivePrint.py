

inp = int(input("enter a no.: "))
num = 0
def wln(num,imp):
    print(num, end = "")
    if num < imp:
        print(",",end = "")
        num += 1
        wln(num,imp)

wln(num,inp)

