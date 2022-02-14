# def myprint(*args, **argkwd):
    # args1 = args

# myprint(10, 20, 30, deco="@", sep="-")
# myprint("python", "javascript", "R", deco="$")
# myprint("가", "나", "다")
# myprint(100)
# myprint(True, 111, False, "abc", deco="&", sep="")
# myprint()

def myprint(*args, **kwargs):
    if len(args) > 0:
        if "deco" in kwargs:
            deco_string = kwargs["deco"]
        else:
            deco_string = "**"
        if "sep" in kwargs:
            sep_string = kwargs["sep"]
        else:
            sep_string = ','

        print(deco_string, end='')
        print(*args, sep=sep_string, end='')
        print(deco_string)
    else:
        print("Hello Python")

myprint(10, 20, 30, deco="@", sep="-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")
myprint()
