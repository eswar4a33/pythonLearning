"""4. Given two sorted list of integers, write a function to merge the two lists.
If a number appears in both the lists, only one copy should be stored."""


ls = [0,1,2,3,4,5,6]
lss = [4,5,6,7,8,9,10]

for i in lss:
    if i not in ls:
        ls.append(i)
print(ls)
