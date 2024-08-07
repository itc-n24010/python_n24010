def a(x=2):
    while True:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
             yield x
        x += 1

i = a()
for n in range(10):
    print(next(i), end=" ")
print("")
