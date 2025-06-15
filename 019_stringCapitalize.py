"""
7. Write your own version of string capitalize
e.g " i  am becoming An Expert in Python" => "I Am Becoming An Expert In Python"
"""
st = " i  am becoming An Expert in Python"

def cap(i):
    if ord(i[0])>=97 and ord(i[0])<=112:
        return chr(ord(i[0])-32)+i[1:]
    else:
        return i

ls = st.split()
ls1 = []
for i in ls:
#    ls1.append(cap(i))
    ls1.append((chr(ord(i[0])-32)+i[1:]) if (ord(i[0])>=97 and ord(i[0])<=112) else i)

print(" ".join(ls1))
