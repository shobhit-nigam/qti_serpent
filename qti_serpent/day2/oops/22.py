class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def __add__(self, other):
        temp = time()
        if type(other) is time:
            tot_min = self.minutes + self.hours*60 + other.minutes + other.hours*60
            temp.hours = tot_min//60
            temp.minutes = tot_min%60

        elif type(other) is int:
            tot_min = self.minutes + self.hours*60 + other
            temp.hours = tot_min//60
            temp.minutes = tot_min%60
        return temp

    def __radd__(self, other):
        temp = time()

        tot_min = self.minutes + self.hours*60 + other
        temp.hours = tot_min//60
        temp.minutes = tot_min%60
        return temp

sun = time(0, 55)
mon = time(1, 35)
total = sun + 20
total.display()
total = sun + mon
total.display()
total = 20 + sun
total.display()

# error
# can be resolved by checking for float
total = sun + 1.30
