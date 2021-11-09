class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it more secure")

class linux(unix):
    def free(self):
        print("the kernel is free")

obju = unix()
obju.cmd()

print("----")

objl = linux()
objl.cmd()
