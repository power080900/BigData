def sumeven(*p):
    sumnum = 0
    if len(p) > 1:
        for data in p:
            if data % 2 == 0:
                sumnum += data
            else :
                sumnum += 0
    else :
        sumnum = -1
    return sumnum
print(sumeven(1,2,3,4,5))
print(sumeven(11,22,33,44,55))
print(sumeven(1,3,5))
print(sumeven())