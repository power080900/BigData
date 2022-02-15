import random

Lotto = []

for i in range (1,100):
    num = random.randint(1, 46)
    if num not in Lotto :
        Lotto.append(num)
    if len(Lotto) == 6:
        break

print("행운의 로또번호 :",Lotto)