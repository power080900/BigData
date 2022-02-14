def print_triangle_withdeco (num, deco= '%') :
    if 1 <= num <= 10 :
        for i in range(1, num+1):
            print(" " * (num-i), deco * i)
    else :
        num = 5
        for i in range (1, num + 1):
            print(" " * (num-i), deco * i)

print_triangle_withdeco(10)
print("-" * 10)
print_triangle_withdeco(100)