# over riding
class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it more secure")

class linux(unix):
    def free(self):
        print("the kernel is free")

    def secure(self):
        print("rwx makes it secure, and extra firewalls too")

obju = unix()
objl = linux()

obju.secure()
print("---")
objl.secure()
