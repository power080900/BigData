def expr (num1 , num2 , cal1) :
    if cal1 == "+" :
        rlt = num1 + num2
        return rlt
    elif cal1 == "-" :
        rlt = num1 - num2
        return rlt
    elif cal1 == "*" :
        rlt = num1 * num2
        return rlt
    elif cal1 == "/" :
        rlt = num1 / num2
        return rlt
    else :
        rlt = None
        return rlt

a = expr(11,22,"@")
if a == None :
    print("수행불가")
else :
    print("연산결과 : ",a)

a = expr(11,22,"+")
if a == None :
    print("수행불가")
else :
    print("연산결과 : ",a)