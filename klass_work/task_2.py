import json
import os


def requester():
    if 'file_name_id_al.json' in os.listdir():
        while True:
            name, i_d, access_level = requests()
            with open('file_name_id_al.json', 'r', encoding='utf-8') as f:
                res:list = json.load(f)
                res.append({'name':name, 'id': i_d, 'access_level': access_level})

            with open('file_name_id_al.json', 'w', encoding='utf-8') as f:
                json.dump(res, f, indent=2)

    else:
        with open('file_name_id_al.json', 'w', encoding='utf-8') as f:
            name, i_d, access_level = requests()
            json.dump([{'name':name, 'id': i_d, 'access_level': access_level}], f, indent=2)
        requester()


def requests():
    name = input('Введите имя:\n')
    i_d = input('Введите id:\n')
    access_level = input('Введите уровень доступа от 1 до 7:\n')
    return name, i_d, access_level





