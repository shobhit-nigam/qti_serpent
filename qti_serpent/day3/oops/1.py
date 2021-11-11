class sample:
    data = 30
    datb = 40

    def funca(self, val):
        self.data = val

    def funcb(self, val):
        self.data = val

    def funcc():
        pass

objs = sample()
print("objs.data =", objs.data)
objs.funca(100)
print("objs.data =", objs.data)

# error
objs.funcc()
