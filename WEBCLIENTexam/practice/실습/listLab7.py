li = [
    [10,20,30,40,50],
    [5,10,15],
    [11,22,33,44],
    [9,8,7,6,5,4,3,2,13]
]

j = 0
for num in li :
    sumnum = 0
    j += 1
    for i in num:
        sumnum += i
    print(j,"행의 합은",sumnum,"입니다.")
