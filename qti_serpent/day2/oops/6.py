# multilevel and multiple

class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it more secure")

class linux(unix):
    def free(self):
        print("the kernel is free")

class android(linux):
    def ui():
        print("great gui to work with")

obju = unix()
objl = linux()
obja = android()

obja.secure()
