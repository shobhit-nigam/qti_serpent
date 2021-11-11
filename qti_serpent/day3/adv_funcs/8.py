lista = [10, 20, 30, 40, 50, 30, 40]
listb = [40, 15, 62, 17, 18, 29, 100]

liste = list(map(lambda x, y: x if x<y else y, lista, listb))

print(liste)
