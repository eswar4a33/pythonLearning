def fibRecur(f,s,n):
    if n != 0:
        print(f, end = " ")
        f , s = s, f+s
        fibRecur(f,s,n-1)


f = 0
s = 1
n = 10
fibRecur(f,s,n)
