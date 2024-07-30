A = {x for x in range(21)}
B = {x for x in range(21) if x % 2 == 0}
print(A)
print(B)

C = A - B
print(C)
