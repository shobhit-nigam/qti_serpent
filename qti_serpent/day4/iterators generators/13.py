def funca(num):
    while True:
        yield num
        num =  num+1

x = funca(11)

# error
print(x[2:7])
