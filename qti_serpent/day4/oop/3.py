from mod import Sample

objs = Sample()

print(objs.calc())
print("----")

def linear(self, val):
    la = self.data + self.datb + val
    return la

Sample.calc = linear
objt = Sample()
print(objt.calc(100))
