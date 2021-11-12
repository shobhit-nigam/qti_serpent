def funca(start=0, end=0, step=1):
    n = start
    while(n < end):
        yield n
        n = n+1

for i in funca(3, 8, 2):
    print(i)
