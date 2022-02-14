# def mydict (**kwargs):
#     mykargs = {}
#     for k, v in kargs.items():
#         mykargs["my" + k] = v
#     return mykargs

def mycompredict(**kwargs):
    mykwargs = {"my" + a : b for a, b in kwargs.items()}
    return mykwargs

print(mycompredict(favoriteFood = '제육볶음', hobby='보드게임'))
print(mycompredict(a=2))
print(mycompredict())