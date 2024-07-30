date = [
    ['0001', 'Male', 'Yamada', 'Tarou', '25', 'Tokyo'],
    ['0002', 'Male', 'Satou', 'Takeshi', '27', 'Kanagawa'],
    ['0003', 'Female', 'Tanaka', 'Yuko', '25', 'Saitama'],
    ['0004', 'Male', 'Suzuki', 'Ichirou', '35', 'Hokkaido']
]

x = {}
for a in date:
    key = a[0]
    information = a[1:]
    x [key] = information

print('number', 'information', sep='\t')
for key, information in x.items():
    print(key, information)
