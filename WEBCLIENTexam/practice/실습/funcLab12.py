# def mydict(**argKwd):
    # keys = argKwd['a']
    # values = argKwd['values']
    # data = dict()
    # for data in argKwd:
    #     if argKwd == 0 :
    #         return data
    #     else :
    #         data = {'my'+keys:values}
    #         return data
#
#
# print(mydict(a ='음식', b ='제육볶음'))

def mydict(**kargs):
    mykargs = {}
    for k, v in kargs.items():
        mykargs["my"+k] = v
    return mykargs

print(mydict(a=2, b=3))
print(mydict(a=2))
print(mydict())