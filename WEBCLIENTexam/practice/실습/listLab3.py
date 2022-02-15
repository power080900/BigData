listnum = [10, 5, 7, 21, 4, 8, 18]
num1 = listnum[0]
num2 = []

for i in range (1,len(listnum)) :
    num2 = listnum[i]
    if num1 > num2 :
        pass
    else :
        num1 = num2

num3 = listnum[0]
num4 = []

for i in range (1,len(listnum)) :
    num4 = listnum[i]
    if num3 < num4 :
        pass
    else :
        num3 = num4

print("최솟값 :",num3,", 최댓값 :",num1)