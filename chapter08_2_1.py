import pathlib
p = pathlib.Path('.')
for pf in p.iterdir():
    if pf.is_file():
        print(str(pf))

print("解答：カレントディレクトリ内のファイルが表示される")
