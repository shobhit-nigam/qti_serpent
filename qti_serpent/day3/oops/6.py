class Celsius:
    def __init__(self, temp=0):
        self.set_temp(temp)

    def to_far(self):
        return self.get_temp() * (9/5) + 32

    def get_temp(self):
        return self.__temp

    def set_temp(self, val):
        self.__temp = val

today = Celsius(27)

print(today.get_temp())

print(today.to_far())

today.set_temp(30)

print(today.get_temp())
