import os

files = os.chdir("c:/iotest/")
files = open("yesterday.txt")


try :
    h = 0
    for i in files:
        i = i.lower()
        if "yesterday" in i:
            h += 1
except FileNotFoundError :
    print("파일을 읽을 수 없어요")
else :
    print("Number of a Word 'yesterday'",h)
finally :
    print("수행완료!!")