weekTem = {'일': ('4','-8')
    ,'월': ('5','-3')
    ,'화': ('2','-8')
    ,'수': ('7','-6')
    ,'목': ('4','-7')
    ,'금': ('3','-8')
    ,'토': ('3','-9')}

weekValue = weekTem.keys()
temValue = weekTem.values()
findWeek = input("요일명을 한글로 입력하세요 :")

if findWeek in weekTem:
    maxTem = max(weekTem[findWeek])
    minTem = min(weekTem[findWeek])
    print(findWeek,"요일의 최저 온도는 ",minTem,'이고, 최고온도는',maxTem,"입니다.")
else :
    print(findWeek,"요일의 정보를 찾을 수 없습니다.")