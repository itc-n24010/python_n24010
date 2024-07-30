date = [
['01', '0001', 'Male', 'Yamada', 'Tarou', '25', 'Tokyo'],
['01', '0002', 'Male', 'Satou', 'Takeshi', '27', 'Kanagawa'],
['01', '0003', 'Female', 'Tanaka', 'Yuko', '25', 'Saitama'],
['02', '0001', 'Male', 'Smith', 'Mike', '22', 'NewJersey'],
['02', '0002', 'Male', 'Turner', 'Tom', '27', 'Kansas'],
['02', '0003', 'Male', 'Jackson', 'David', '25', 'Florida']
]

x = {}
for a in date:
    key = a[0], a[1]
    information = a[2:]
    x[key] = information

print('number', 'information', sep='\t')
for key, information in x.items():
    print(key, information)
