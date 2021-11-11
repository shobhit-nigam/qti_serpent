lista = [10, 20, 30, 40, 50]
listb = [4, 5, 6, 7, 8, 9, 10, 11]

def calc(la, lb):
    return 2*la + lb**2 - 10

liste = list(map(lambda la, lb: 2*la + lb**2 - 10, lista, listb))

print(liste)
