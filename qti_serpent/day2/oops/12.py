# multilevel and multiple

class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it more secure")

    def __init__(self):
        print("init of unix")

class linux(unix):
    def free(self):
        print("the kernel is free, and also open source")

# overriding the init
    def __init__(self):
        print("init of linux")

#obju = unix()
#print("----")
objl = linux()
objl.__init__()
