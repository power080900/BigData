import random

num = [random.randint(0,100) for i in range(1,11) ]
# for i in range(1,11):
#     a = random.randint(0,100)
#     num.append(a)

# score = dict()
# for i in num:
#     if i >= 60:
#         score[i] = 'pass'
#     else:
#         score[i] = 'nopass'
# print(score)

score = {i: 'pass' if i >=60 else 'nopass' for i in num}
print(score)
# score_nopass={i for i in num if i < 60}
# print(score_nopass)