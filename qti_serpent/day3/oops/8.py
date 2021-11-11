class Celsius:
    def __init__(self, temp=0):
        self.temp = temp

    def to_far(self):
        return self.temp * (9/5) + 32

    def get_temp(self):
        print("getting temp")
        return self.__temp

    def set_temp(self, val):
        print('setting temp')
        if val < -273.25:
            raise ValueError("temperature below absolute zero is not possible")
        self.__temp = val

    temp = property(get_temp, set_temp)

today = Celsius(27)
print("---")
print(today.temp)
print("---")
print(today.to_far())
print("---")
today.temp = 30
print("---")
print(today.temp)
