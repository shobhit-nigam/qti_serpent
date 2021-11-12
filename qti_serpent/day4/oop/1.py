class Sample:
    data = 33
    datb = 44

    def calc(self):
        la = self.data ** 2 + self.datb * 2 + 5
        return la

    def funca(self):
        self.datc = 100

objs = Sample()
objt = Sample()

print("objs.data =", objs.data)
print("objs.data =", objs.datb)
print("objt.data =", objt.data)
print("objt.data =", objt.datb)
print("----")
objs.funca()
print("objs.datc =", objs.datc)
# error
print("objt.datc =", objt.datc)
