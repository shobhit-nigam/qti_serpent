# type

class avenger:
    ranking = 0
    strength = None

    def fight(manish):
        print("uses", manish.strength)

thor = avenger()
wanda = avenger()

print(thor.ranking)

#error
thor.fight()
# translates to
# avenger.fight(thor)

#error
wanda.fight()
# translates to
# avenger.fight(wanda)
