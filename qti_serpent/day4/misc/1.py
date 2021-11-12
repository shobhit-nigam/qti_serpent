import time

size = 8000000

lista = range(size)
listb = range(size)

# for loop
startTime = time.time()
res = []
for i in range(len(lista)):
    res.append(lista[i] * listb[i])
endTime = time.time()
print("time taken by for loop:", endTime-startTime)

# list comprehension
startTime = time.time()
res = [lista[i] * listb[i] for i in range(len(lista))]
endTime = time.time()
print("time taken by list comprehension:", endTime-startTime)

# map function
startTime = time.time()
def mul(la, lb):
    return la*lb
res = list(map(mul, lista, listb))
endTime = time.time()
print("time taken by map:", endTime-startTime)

# map function with lambda
startTime = time.time()
res = list(map(lambda la, lb: la*lb, lista, listb))
endTime = time.time()
print("time taken by map and lambda:", endTime-startTime)
