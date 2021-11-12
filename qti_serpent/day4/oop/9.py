class Bird:
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        print("using get item method")
        return self.__dict__[item] + " birdie"

    def __setitem__(self, key, value):
        print("using get item method")
        self.__dict__[key] = value

    def __delitem__(self, item):
        del self.__dict__[key]


dove = Bird("plucky")

print(dove.name)
print("----")
print(dove["name"])
dove["name"] = "fluffy"
