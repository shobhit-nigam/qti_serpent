lista = [10, 20, 30, 40, 50]
listb = [4, 5, 6, 7, 8, 9, 10, 11, 12]
listc = ['e', 'a', 'r', 't', 'h', ' ', 'p', 'e', 'a', 'c', 'e']

def only_vowels(ch):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ch in vowels

listd = list(filter(lambda ch: ch in ['a', 'e', 'i', 'o', 'u'], listc))

print(listd)

liste = list(filter(lambda x: x%2==0 and x%3==0, listb))
print(liste)
