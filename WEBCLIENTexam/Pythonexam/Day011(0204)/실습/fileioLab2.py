import os

files1 = os.chdir("c:/iotest/")
files1 = open("sample.txt","rt", encoding="UTF-8")

files2 = os.chdir("c:/iotest/")
files2 = open("sample_yyyy_mm_dd.txt", "at", encoding="UTF-8")

a = files1.read()
files2.write(a)

with open("sample_yyyy_mm_dd.txt", "rt", encoding="UTF-8") as files2:
    try :
        b = files2.read()
    finally :
        print(b)
        print("저장이 완료되었습니다")

files1.close()
files2.close()
