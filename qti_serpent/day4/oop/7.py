class Bird:
    def __init__(self, name):
        self.name = name

dove = Bird("plucky")

print(dove.name)
print(dove.__dict__)
