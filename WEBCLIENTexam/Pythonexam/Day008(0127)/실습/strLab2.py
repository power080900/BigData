s1 = "pythonjavascript"
s2 = "010-7777-9999"
s3 = "PYTHON"
s4 = "Python"
s5 = "https://www.python.org/"
s6 = '891022-2473837'
s7 = '100'
s8 = 'The Zen of Python'

print("1번 :", len(s1))
print("2번 :", s2.replace("-",""))
print("3번 :", s3[::-1])
print("4번 :", s4.lower())
print("5번 :", s5[8:-1])
if int(s6[7]) == 1 or int(s6[7]) == '3' :
    print("6번 :", "남성")
else :
    print("6번 :", "여성")
print("7번 :", int(s7), ",", float(s7))
print("8번 :", s8.count("n"))
print("9번 :", s8.index("Z"))

S8 = s8.upper()
print("10번 :",S8.split(' '))