a = 'python_test.txt'
b = 'Hello out_test.txt'

with open(a, 'w') as x:
    x.write(b)

with open(a, 'r') as x:
    for line in x:
        print(line, end="\n")
