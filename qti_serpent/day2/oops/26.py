class sample:
    def funca():
        la = 33
        lb = 44
        return dir()

    ca = 34
    cb = 45


objs = sample()
print(dir(objs))
print("---")
print(sample.__dict__)
