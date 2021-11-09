# type

class avenger:
    ranking = 0
    strength = None

    def fight(self):
        print("uses", self.strength)

thor = avenger()
wanda = avenger()

print(thor.ranking)

#error
thor.fight()
# translates to
# avenger.fight(thor)

wanda.strength = "magic"

#error
wanda.fight()
# translates to
# avenger.fight(wanda)
