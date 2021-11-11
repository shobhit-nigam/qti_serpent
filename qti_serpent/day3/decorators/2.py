def funca():
    print("in funca")
    def funcb():
        print("in funcb")
    funcb()
    print("in funca")

funca()
