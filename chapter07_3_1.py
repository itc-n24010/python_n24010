face_part = {1: '目', 2: '鼻', 3: '口', 4: '眉', 5: '耳'}

class MyDictKeyError(Exception):
    def __init__(self, key):
        self.key = key
    def __str__(self):
        return '登録されていません {0}'.format(self.key)

def get_dict_value(dict_tbl, key):
    if key not in dict_tbl:
        raise MyDictKeyError(key)
    else:
        return dict_tdl[key]

my_dict = {1: '目', 2: '鼻', 3: '口'}

try:
    my_dict = get_dict_value(my_dict, 5)
except MyDictKeyError as e:
    print(e)
    key = e.args[0]
    my_dict[key] = face_part[key]
    print(key, face_part[key], 'を my_dictに追加しました')
    face_part = face_part[key]

print(face_part)
