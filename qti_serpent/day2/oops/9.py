# multilevel and multiple

class unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it more secure")

class linux(unix):
    def free(self):
        print("the kernel is free, and also open source")

class mobileOS:
    def portable(self):
        print("can be ported to various devices")

    def free(self):
        print("the os is free")

class android(mobileOS, linux, list):
    def ui(self):
        print("great gui to work with")

obju = unix()
objl = linux()
obja = android()

obja.free()
