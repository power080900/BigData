import random

lotto = set()

while len(lotto) < 6:
    a = random.randint(1,46)
    lotto.add(a)

print("행운의 로또번호 :",lotto)