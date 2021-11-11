class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def __call__(self):
        print("made time object callable")
        return f"{self.hours} hours and {self.minutes} minutes"

sun = time(0, 55)
mon = time(1, 35)

#no error
print(sun())
