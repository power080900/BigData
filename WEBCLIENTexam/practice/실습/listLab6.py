li = [
    [10,12,14,16],
    [18,20,22,24],
    [26,28,30,32],
    [34,36,38,40]
]

print("1행 1열의 데이터 :",li[0][0])
print("3행 4열의 데이터 :",li[2][3])
print(len(li))
print(len(li[0]))
print("3행의 데이터들 :",li[1])

col1 = []
for i in range(len(li)):
    col1.append(li[i][1])
print("2열의 데이터들 :",col1)

ldia = []
for i in range(len(li)):
    ldia.append(li[i][i])
print("왼쪽 대각선 데이터들 :",ldia)

rdia = []
for i in range(len(li)):
    rdia.append(li[i][3-i])

print("오른쪽 대각선 데이터들 :",rdia)