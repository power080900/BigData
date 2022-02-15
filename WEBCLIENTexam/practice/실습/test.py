for i in range(1, 10) :
    for j in range(i) :
        print('#', end = '')
    print()

age = int(input("너 몇 살이니? "))
if age < 19:
    print("애들은 가라")
