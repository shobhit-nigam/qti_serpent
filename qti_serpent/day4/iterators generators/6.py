class rangex:
    def __init__(self, num):
        self.i = 0
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.num:
            val = self.i
            self.i = self.i + 1
            return val
        else:
            raise StopIteration()


for i in rangex(4):
    print(i)
