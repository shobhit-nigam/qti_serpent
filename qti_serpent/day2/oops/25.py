class sample:
    def funca():
        la = 33
        lb = 44
        return dir()

    ca = 34
    __cb = 45

    def __dir__(self):
        return ['ca', 'funca']




objs = sample()
print(dir(objs))
