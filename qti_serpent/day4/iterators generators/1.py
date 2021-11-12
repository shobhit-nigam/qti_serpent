lista = [10, 13, 15]

it = iter(lista)
            # lista.__iter__()

print(next(it))
            # it.__next__()

print(next(it))
print(next(it))

# error
print(next(it))
            # StopIteration
