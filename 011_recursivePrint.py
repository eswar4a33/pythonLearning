def wln(first,last):
    print(first, end = "")
    if first < last:
        print(",",end = "")
        first += 1
        wln(first,last)

start = int(input('enter the starting no.: '))
end = int(input('enter the last no.: '))
          

wln(start,end)
