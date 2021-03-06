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


sun = time(0, 55)
mon = time(1, 35)
tue = time(1, 45)

total = sun + 20
total.display()

total = sun + mon
total.display()
