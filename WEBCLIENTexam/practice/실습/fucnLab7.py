def print_gugudan (num1) :
    if type(num1) != int :
        return
    elif 1 <= num1 <= 9 :
        print(num1, "단")
        for i in range (1, 10) :
            print(num1, "*", i, "=", num1*i)
    else :
        return

print_gugudan(5)