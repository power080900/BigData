listnum = [10 , 5 , 7 , 21 , 4 , 8 , 18]
num1 = listnum[0]
num2 = []

for i in range (1,len(listnum)):
    num2 = listnum[i]
    if num1 < num2 :
        pass
    else :
        num1 = num2

print("최솟값 :",num1)