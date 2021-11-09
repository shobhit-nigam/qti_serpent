class bank:
    def __init__(self, a=0, o=0, n="John Doe"):
        self.accNum = a
        self.opnBal = o
        self.curBal = self.opnBal
        self.cusName = n

    def display(self):
        print("welcome", self.cusName)
        print("your acount balance is", self.curBal)

    def deposit(self, amt):
        self.curBal = self.curBal + amt
        print("deposit is successfull")

    def withdraw(self, amt):
        if self.curBal > amt:
            print("withdrawal is successfull")
            self.curBal = self.curBal - amt
        else:
            print("not enough funds")


obja = bank(28650, 1000, "Robert Downey")
objb = bank(28660, 1000, "Chris evans")

obja.display()
print("-----")
obja.withdraw(400)
print("-----")
obja.display()
