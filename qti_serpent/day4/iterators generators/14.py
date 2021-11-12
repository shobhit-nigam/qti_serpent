import itertools

#help(itertools)


def funca(num):
    while True:
        yield num
        num =  num+1

x = funca(11)



for val in itertools.islice(funca(11), 2, 7):
    print(val)

# error
print(x[2:7])
