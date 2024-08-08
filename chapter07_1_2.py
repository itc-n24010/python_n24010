def list_average(a):
    try:
        return sum(a)/len(a)
    except:
        print('list_lenght:', len(a))
        return None

print(list_average([1.7, 2.9, 2,3]))
print(list_average([]))
