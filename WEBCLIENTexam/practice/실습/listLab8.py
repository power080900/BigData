li = [
    ['B','C','A','A'],
    ['C','C','B','B'],
    ['D','A','A','D']
]

cntA = 0
for strA in li:
    for i in strA:
        if 'A' in i:
            cntA += 1
print('A는 ', cntA, '개 입니다.')

cntB = 0
for strB in li:
    for i in strB:
        if 'B' in i:
            cntB += 1
print('B는 ', cntB, '개 입니다.')

cntC = 0
for strC in li:
    for i in strC:
        if 'C' in i:
            cntC += 1
print('C는 ', cntC, '개 입니다.')

cntD = 0
for strD in li:
    for i in strD:
        if 'D' in i:
            cntD += 1
print('D는 ', cntD, '개 입니다.')