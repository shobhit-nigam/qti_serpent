class avenger:
    ranking = 0
    strength = None

    def fight(self):
        print("uses", self.strength)

thor = avenger()
wanda = avenger()

thor.ranking = 40

print("avenger ranking =", avenger.ranking)
print("thor ranking =", thor.ranking)
print("wanda ranking =", wanda.ranking)

print("-----")

avenger.ranking = 20

print("avenger ranking =", avenger.ranking)
print("thor ranking =", thor.ranking)
print("wanda ranking =", wanda.ranking)
