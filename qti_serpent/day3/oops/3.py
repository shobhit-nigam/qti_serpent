class sample:
    data = 30
    datb = 40

    def funca(self, val):
        self.data = val

    @classmethod
    def funcb(self, val):
        self.data = val

    def funcc():
        pass

objs = sample()
print("objs.data =", objs.data)
objs.funcb(100)
print("objs.data =", objs.data)

objt = sample()
print("objt.data =", objt.data)

# error
#objs.funcc()
