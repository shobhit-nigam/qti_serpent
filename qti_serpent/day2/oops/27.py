class sample:
    def funca():
        la = 33
        lb = 44
        return dir()

    ca = 34
    cb = 45

objs = sample()

print(objs.ca)
print("---")
#error
print(objs.Ca)
