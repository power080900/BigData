def number_all_sum (*p):
    sumnum = 0
    if len(p) >= 1:
        for data in p:
            if type(data) == int:
                sumnum += data
            else:
                sumnum += 0
        # else:
        #     sumnum = None
    else :
        sumnum = None
    if sumnum == 0 :
        sumnum = None
    return sumnum

print(number_all_sum(1, 2, 3, 4, 5))
print(number_all_sum(1, 2, 'a', 3, 4, 'b', 5))
print(number_all_sum(10, 20, True))
print(number_all_sum())
print(number_all_sum('a', True, '가'))