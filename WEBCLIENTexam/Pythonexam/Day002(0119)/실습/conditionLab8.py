import random
oper_num = random.randint(1,10)
if oper_num % 5 == 1 :
    cal_num = 300 + 50
elif oper_num % 5 == 2 :
    cal_num = 300 - 50
elif oper_num % 5 == 3 :
    cal_num = 300 * 50
elif oper_num % 5 == 4 :
    cal_num = 300 / 50
elif oper_num % 5 == 0 :
    cal_num = 300 % 50

print("결과값 :",cal_num)