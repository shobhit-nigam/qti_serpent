class Bird:
    def walk(self):
        print("I can walk")

    def fly(self):
        print("I can fly")

class ToyBird:
    def walk(self):
        print("I can walk")

    def fly(self):
        print("I can fly")

def bird_testing(x):
    try:
        x.walk()
        x.fly()
    except AttributeError:
        print("i am not a bird")
    else:
        print("i am a bird")

dovetoy = ToyBird()

print(isinstance(dovetoy, Bird))

# duck typing
bird_testing(dovetoy)
