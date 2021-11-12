#with open("hello.txt", "r") as fa:
#    stra = fa.read()


class Sample:
    def __init__(self):
        print("init")

    def __enter__(self):
        print('calling enter method')
        print("necessary steps")

    def __exit__(self, exception_type, exception_value, traceback):
        print('calling exit method')
        print("necessary steps for exiting")

    def __del__(self):
        print("del called")

with Sample() as objs:
    # some code
    print("with statement")
    import time
    print("---")
    time.sleep(5)
