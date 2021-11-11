def star(gen):
    def inner(*args):
        print("*********")
        gen(*args)
        print("*********")
    return inner

def hash(gen):
    def inner(*args):
        print("#########")
        gen(*args)
        print("#########")
    return inner

@star
@hash
def display(statement):
    print(statement)

display("hello world")
