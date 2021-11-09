class sample:
    def funca():
        la = 33
        lb = 44
        return dir()

    ca = 34
    cb = 45

    def __getattr__(self, other):
        print(f"class sample does not have {other} attribute")
        print('you probably meant "ca"')
        return self.ca

objs = sample()

print(objs.ca)
print("---")
#error
print(objs.Ca)
