while True :
    month = int(input("1~12 사이의 값을 입력하세요 >> "))
    if month == 12 or month == 1 or month == 2 :
        weather = "겨울"
        print(month,"월은",weather)
    elif month == 3 or month == 4 or month == 5 :
        weather = "봄"
        print(month, "월은", weather)
    elif month == 6 or month == 7 or month == 8 :
        weather = "여름"
        print(month, "월은", weather)
    elif month == 9 or month == 10 or month == 11 :
        weather = "가을"
        print(month, "월은", weather)
    else :
        print("1~12 사이의 값을 입력하세요!")
        break