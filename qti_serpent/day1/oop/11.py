class bank:
    accNum = 0
    opnBal = 0
    curBal = opnBal
    cusName = "John Doe"

    def __init__(self):
        print("hi from init")

    def update(self, a, o, n):
        self.accNum = a
        self.opnBal = o
        self.curBal = self.opnBal
        self.cusName = n

    def display(self):
        print("welcome", self.cusName)
        print("ypur acount balance is", self.curBal)


obja = bank()
objb = bank()

print("-----")
obja.update(28650, 1000, "Robert Downey")

obja.display()
print("-----")
objb.display()
