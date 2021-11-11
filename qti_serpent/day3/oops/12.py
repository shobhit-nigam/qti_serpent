class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def __repr__(self):
        return f"time(hours={self.hours}, minutes ={self.minutes})"

    def __str__(self):
        return f"{self.hours} hours and {self.minutes} minutes"

sun = time(0, 55)
mon = time(1, 35)

print(sun)
