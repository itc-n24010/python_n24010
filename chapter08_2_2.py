import pathlib
p = pathlib.Path('.')
for a in p.glob('a*'):
    if a.is_dir():
        print(a)
