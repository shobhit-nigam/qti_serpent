class Sample:
    data = 100
    _datb = 200
    __datc = 300
    __datd__ = 400

    def display(self):
        print("data =", self.data)
        print("_datb =", self._datb)
        print("__datc =", self.__datc)
        print("__datd__ =", self.__datd__)

objs = Sample()


print("data =", objs.data)
print("_datb =", objs._datb)
# error
# print("__datc =", objs.__datc)
print("__datd__ =", objs.__datd__)
print("----")

objs.display()
