import pickle
import json
import os


def search_from_json_to_pickle():
    for i in os.listdir():
        if i.split('.')[-1] == 'json':
            new_file_name = i.split('.')
            new_file_name[-1] = 'pickle'
            new_file_name = '.'.join(new_file_name)
            print(new_file_name)
            with (open(i, 'r', encoding='utf-8') as f_1,
                  open(new_file_name, 'wb') as f_2):
                obj = json.load(f_1)
                pickle.dump(obj, f_2)

