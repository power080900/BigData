def print_triangle (n1) :
    if 1 <= n1 <= 10 :
        for i in range(n1, 0,-1) :
            print("@" * i)
    else :
        return

print_triangle(10)