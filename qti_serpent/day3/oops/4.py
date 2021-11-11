class sample:
    data = 30
    datb = 40

    def funca(self, val):
        self.data = val

    @staticmethod
    def funcc():
        pass

objs = sample()
#no error
objs.funcc()

# objs.funcc() = sample.funcc()
