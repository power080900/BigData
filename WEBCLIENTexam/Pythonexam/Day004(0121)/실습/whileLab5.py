while True:
    word = input("문자를 입력하세요 >> ")
    wordlength = len(word)
    if wordlength == 0 :
        break
    elif wordlength < 5 :
        print("유효한 입력 결과 : *",word,"*",sep='')
    elif 5 <= wordlength <= 8 :
        continue
    elif wordlength > 8 :
        print("유효한 입력 결과 : $",word,"$",sep='')