import json


def f(a, b):
    with open(a, 'r', encoding='utf-8') as f:
        res = list(map(lambda x: x.capitalize()[0:-1], f.readlines()))


    with open(b, 'w+') as f1:
        json.dump(res, f1, indent=2)

