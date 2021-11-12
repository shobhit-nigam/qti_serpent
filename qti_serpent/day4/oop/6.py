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

class Animal:
    def walk(self):
        print("I can walk")

def bird_testing(x):
    try:
        x.walk()
        x.fly()
    except AttributeError:
        print("i am not a bird")
    else:
        print("i am a bird")

cat = Animal()

print(isinstance(cat, Bird))

# duck typing
bird_testing(cat)
