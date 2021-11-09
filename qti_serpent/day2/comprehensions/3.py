lista = [11, 22, 33, 44, 55, 66, 77]

listb = []
for val in lista:
    if val%2 == 0:
        listb.append(val)

listc = [val if val%2 == 0 else 2 for val in lista ]

print("lista =", lista)
print("listb =", listb)
print("listc =", listc)
