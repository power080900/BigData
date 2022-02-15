import random

countn = 1

while True :
    num1 = int(random.randint(0, 30))
    ascii1 = chr(64+num1)
    if num1 == 0 :
        print("수행 횟수는", countn-1, "번 입니다.")
        break
    elif num1 >=27 :
        print("수행 횟수는", countn-1, "번 입니다.")
        break
    else :
        print(ascii1,"(",num1,")", sep='')
        countn += 1
