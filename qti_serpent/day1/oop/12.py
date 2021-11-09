class bank:
    accNum = 0
    opnBal = 0
    curBal = opnBal
    cusName = "John Doe"

    def __init__(self, a=0, o=0, n="John Doe"):
        self.accNum = a
        self.opnBal = o
        self.curBal = self.opnBal
        self.cusName = n

    def display(self):
        print("welcome", self.cusName)
        print("your acount balance is", self.curBal)


obja = bank(28650, 1000, "Robert Downey")
objb = bank()

print("-----")

obja.display()
print("-----")
objb.display()
