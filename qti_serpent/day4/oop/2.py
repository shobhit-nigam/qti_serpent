from mod import Sample

objs = Sample()

print(objs.calc())
print("----")

def linear(self):
    la = self.data + self.datb
    return la

Sample.calc = linear
objt = Sample()
print(objt.calc())
