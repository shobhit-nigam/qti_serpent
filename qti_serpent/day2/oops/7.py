# multilevel and multiple

class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it more secure")

class linux(unix):
    def free(self):
        print("the kernel is free")

class mobileOS:
    def portable(self):
        print("can be ported to various devices")

class android(linux, mobileOS):
    def ui(self):
        print("great gui to work with")

obju = unix()
objl = linux()
obja = android()

obja.portable()
