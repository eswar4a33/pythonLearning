"""8. Serialize a nested list for e.g [1,[2,3],[4,5,7],8,[9,10]]
should become [1,2,3,4,5,6,7,8,9,10]"""

ls = [1,[2,3],[4,[5,6,7]],8,[9,10]]

def srt(ls):
    lss = []
    i = 0
    while i != len(ls):
        if type(ls[i]) == list:
            for j in srt(ls[i]):
                lss.append(j)
        else:
            lss.append(ls[i])
        i += 1
    return lss

print(srt(ls))



