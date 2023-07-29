import csv
import json
import os
import pickle


def func_recursive_traversal_and_result(path):  # сохраняет вложенность в виде дерева для json.
    res = []
    for i in os.listdir(path):
        os.chdir(path)
        if os.path.isdir(i):
            p_d = os.getcwd().split('\\')[-1]
            res.append([{'Name': i, 'Type': 'Dir', 'Parent dir': p_d, 'Size': dir_size(os.getcwd())},
                        func_recursive_traversal_and_result(f'{path}\\{i}')])
        else:
            p_d = os.getcwd().split('\\')[-1]
            res.append([{'Name': i, 'Type': 'File', 'Parent dir': p_d, 'Size': os.path.getsize(i)}])
    return res


def f(lll):  # убирает вложенность для записи в csv
    res_2 = []
    def f_2(ll):
        for i in ll:
            if type(i) == list:
                f_2(i)
            else:
                res_2.append(i)

    f_2(lll)
    return res_2


def dir_size(path):  # подсчет размера папки
    res = 0
    for i in os.listdir(path):
        os.chdir(path)
        if os.path.isdir(i):
            res += dir_size(f'{path}\\{i}')
        else:
            res += os.path.getsize(i)
    return res


result = func_recursive_traversal_and_result('C:\\Users\\pollove\\Desktop\\Home_work_8_py_sem\\home_work')

# запись json
with open('json_obj.json', 'w', encoding='utf-8') as f_1:
    json.dump(result, f_1, indent=2)

# запись csv
with open('csv_obj.csv', 'w', newline='') as f_1:
    csv_w = csv.DictWriter(f_1, fieldnames=['Name', 'Type', 'Parent dir', 'Size'])
    csv_w.writeheader()
    csv_w.writerows(f(result))

# запись pickle
with open('pickle_obj.pickle', 'wb') as f_1:
    pickle.dump(result, f_1)
