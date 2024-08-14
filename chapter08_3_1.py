import collections
a = 'なまむぎ・なまごめ・なまたまご'
count = collections.Counter(a)
part = collections.defaultdict(list)
for x, y in count.items():
    part[y].append(x)
print(part[1])
