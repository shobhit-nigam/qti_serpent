import itertools

lista = ['ind', 'nz', 'pak', 'afg']

from itertools import combinations

for game in combinations(lista, 2):
    print(game)
