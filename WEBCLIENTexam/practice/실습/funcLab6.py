def differtwovalue(n1,n2) :
    if n1 == n2 :
        n3 = 0
        return n3
    elif n1 > n2 :
        n3 = n1 - n2
        return n3
    elif n1 < n2 :
        n3 = n2 - n1
        return n3

import random
for i in range(5):
    a = int(random.randint(1,30))
    b = int(random.randint(1,30))
    c = differtwovalue(a,b)
    print(a,"와",b,"의 차는",c,"입니다.")
