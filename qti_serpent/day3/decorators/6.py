rava = "rava"
choco = "choco"
kaju = "kaju"

def laddu(x):
    print("making", x, "laddoos")

def barfi(x):
    print("making", x, "barfi")


def make(gen, x):
    gen(x)

# higher order function
make(laddu, rava)
print("---")
make(barfi, choco)
