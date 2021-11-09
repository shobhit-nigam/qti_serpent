varx = 33
vary = 100

def funca():
    la = 33
    lb = 44
    return dir()

listx = dir()
print("available in entire code:\n",listx)
print("-----")
listy = funca()
print("available in  funca:\n",listy)
