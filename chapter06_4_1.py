import random
random.seed(1)
msgs = ["Hi", "Hello", "Good Morning", "Good Night", "See You Later", "How Are You", "Have A Good Day"]
with open("some.txt","w") as f:
    for i in range(10):
        f.write("{}, {}\n".format(i, random.choice(msgs)))

f = open('some.txt')
a = 0
for x in f:
    print(x, end='')
    if a == 2:
        break
    a += 1
f.close()
