# type
# class names can be used directly

class avenger:
    ranking = 0
    strength = None

    def fight(self):
        print("uses", self.strength)

obja = avenger()

print(avenger.ranking)
avenger.ranking = 100
print(avenger.ranking)

objb = avenger()

print(objb.ranking)
