color = {'red':'#ff0000'
        , 'blue':'#000ff'
        , 'green':'#008000'
        , 'yellow':'#ffff00'
        , 'orange':'#ffa500'
        , 'black':'#000000'
        , 'white':'#ffffff'
        , 'violet':'ee82ee'
        , 'pink':'#ffc0cb'
        , 'lime':'00ff00'
        }

colorKey = color.keys()
findColor = input("칼라명을 영문으로 입력하세요 :")
findValue = color[findColor]

if findColor in colorKey:
    print(findColor,"칼라의 RGB 값은",findValue,"입니다")
else :
    print(findColor, "칼라의 RGB 값을 찾을 수 없습니다")