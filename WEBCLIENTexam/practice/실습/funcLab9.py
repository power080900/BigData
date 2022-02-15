def isPYTHON(string):
    if 'PYTHON' in string :
        return True
    else :
        return False

if isPYTHON("나는 PYTHON을 학습합니다."):
    print('PYTHON이 존재합니다.')
else:
    print('PYTHON이 존재하지 않습니다')

if isPYTHON("나는 python을 학습합니다."):
    print('PYTHON이 존재합니다.')
else:
    print('PYTHON이 존재하지 않습니다')

if isPYTHON("PYTHON1234"):
    print('PYTHON이 존재합니다.')
else:
    print('PYTHON이 존재하지 않습니다')