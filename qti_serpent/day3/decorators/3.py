def funca():
    print("in funca")
    def funcb():
        print("in funcb")
    print("in funca")
    return funcb

x = funca()
# x = funcb
# error
funcb()
