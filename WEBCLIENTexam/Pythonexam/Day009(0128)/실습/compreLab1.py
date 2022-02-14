def createlist (*args, type=1):
    num = list()
    if len(args) > 0:
        if type == 1:
            num = [i for i in args]
        elif type == 2:
            num = [i for i in args if i % 2 == 0]
        elif type == 3:
            num = [i for i in args if i % 2 == 1]
        elif type == 4:
            num = [i for i in args if i >= 10]
        return num
    else :
        if type == 1:
            num = [i for i in range(1, 31)]
        elif type == 2:
            num = [i for i in range(1, 31) if i % 2 == 0 ]
        elif type == 3:
            num = [i for i in range(1, 31) if i % 2 == 1]
        elif type == 4:
            num = [i for i in range(1,31) if i >= 10]
        return num


print(createlist(1,2,3,4,5,10,20,30,40,50,type=2))
print(createlist())
print(createlist(type=3))