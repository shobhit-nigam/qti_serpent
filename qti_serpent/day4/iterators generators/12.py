class Count:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        num = self.start
        while num > 0:
            yield num
            num = num - 1

    def __reversed__(self):
        num = 1
        while num <= self.start:
            yield num
            num = num + 1

#reversed()

for val in Count(3):
    print(val)

for val in reversed(Count(3)):
    print(val)
