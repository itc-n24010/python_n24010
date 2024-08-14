import json

name_list = {
        'Tanaka':{
            '年齢':20,
            '血液型':'A',
            '性別':'男性'
        },
        'Satou':{
            '年齢':19,
            '血液型':'O',
            '性別':'女性'
        },
        'Suzuki':{
            '年齢':20,
            '血液型':'AB',
            '性別':'男性'
        }
}

with open('name_list.json', 'w') as a:
    json.dump(name_list, a)

with open('name_list.json', 'r') as b:
    name = json.load(b)

for key, val in name.items():
    print(key,val)
