# type
# class names can be used directly

fa = 123.67
# error as ranking does not have a value

class avenger:
    ranking
    strength = None

    def fight(self):
        print("uses", self.strength)

obja = avenger()

print(avenger.ranking)
avenger.ranking = 100
print(avenger.ranking)

objb = avenger()

print(objb.ranking)
