import random


while True :
    pairNum1 = int(random.randint(1, 6))
    pairNum2 = int(random.randint(1, 6))
    print("1번 숫자 :",pairNum1)
    print("2번 숫자 :",pairNum2)
    if pairNum1 > pairNum2 :
        print(pairNum1,"이",pairNum2,"보다 크다.")
    elif pairNum1 < pairNum2 :
        print(pairNum1, "이", pairNum2, "보다 작다.")
    elif pairNum1 == pairNum2:
        print("게임 끝")
        break