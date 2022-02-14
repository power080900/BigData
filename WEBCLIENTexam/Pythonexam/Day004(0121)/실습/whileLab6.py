while True :
    num1 = int(input("숫자를 입력하세요 >> "))
    start = 1
    if num1 == 0 :
        print("종료")
        break
    elif num1 < -10 :
        continue
    elif num1 > 10 :
        continue
    elif 0 < num1 < 10 :
        print("입력값 :",num1)
        for i in range (1,num1+1):
            start *= i
        print(start)
    elif -10 < num1 < 0 :
        print("입력값(부호변경) :", num1*-1)
        for i in range (1,(num1*-1)+1):
            start *= i
        print(start)