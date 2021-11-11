class Celsius:
    def __init__(self, temp=0):
        self.temp = temp

    def to_far(self):
        return self.temp * (9/5) + 32

today = Celsius()

today.temp = 27

print(today.temp)

print(today.to_far())

#print(today.__dict__)
