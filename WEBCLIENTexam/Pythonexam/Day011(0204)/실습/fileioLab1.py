import datetime
import os
import calendar
now = datetime.datetime.now()
week = calendar.weekday(now.year, now.month, now.day)
yoil = ['월', '화', '수', '목', '금', '토', '일']

files = os.chdir("c:/iotest/")
files = open("today.txt","wt")
files.write(f"""오늘은 %d년 %d월 %d일입니다.
오늘은 {yoil[week]}요일입니다.
나는 {yoil[week]}요일에 태어났습니다.""" %(now.year, now.month, now.day)
)
files.close()
files = open("today.txt","rt")
for i in files:
    print(i, end = '')
files.close()
print()
print("저장이 완료되었습니다")
