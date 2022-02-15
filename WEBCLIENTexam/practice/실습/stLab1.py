import calendar

while True :
    year = (input("알고 싶은 년도를 입력하세요 >>"))
    month = (input("알고 싶은 월을 입력하세요 >>"))
    try :
        print(calendar.month(int(year), int(month)))
        break
    except ValueError:
        print("잘못된 값을 입력하셨습니다")




# if year == int:
#
# else :
#     print("")