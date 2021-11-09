class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

sun = time(0, 55)
mon = time(1, 35)
total = time()

sun.display()

# error
total = sun + mon
