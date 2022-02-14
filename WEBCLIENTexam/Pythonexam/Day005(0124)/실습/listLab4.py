import random
listnum = [] # 2번

for i in range (1,11) :
    listnum.append(random.randint(1,50)) # 3번
print("4번 :", listnum) # 4번
for i in range (1,10) :
    if listnum[i] <= 10:
        listnum[i] = 100 #5번
print("6번 :",listnum) # 6번
print("7번 :",listnum[0]) # 7번
print("8번 :",listnum[9]) # 8번
print("9번 :",listnum[1:6]) # 9번
print("10번 :",listnum[::-1]) # 10번
print("11번 :",listnum[0:]) # 11번
listnum[4:5] = [] # 12번
print("12번 :",listnum[0:]) # 13번
listnum[2:4] = [] # 14번
print("13번 :",listnum[0:]) # 15번