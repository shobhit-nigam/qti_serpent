class bank:
    def __init__(self, a=0, o=0, n="John Doe"):
        self.accNum = a
        self.opnBal = o
        self.curBal = self.opnBal
        self.cusName = n
        self.__rating = 3

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

    def __calcRating(self):
        # criteria 1
        # criteria 2
        # criteria 3
        self.__rating = self.curBal//500 + self.__rating


    def loan(self):
        self.__calcRating()
        if self.__rating > 0 and self.__rating < 5:
            print("you can get a loan of", self.__rating * 1000)
        else:
            print("you can get a loan of", self.__rating * 2000)


obja = bank(28650, 1000, "Robert Downey")
objb = bank()

obja.loan()
obja.deposit(2500)
obja.loan()

# error
print(obja.__rating)
