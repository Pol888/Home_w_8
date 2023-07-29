import csv
import pickle


def f():
    with open('task_4_json_file.csv', 'r', newline='') as f_1:
        csv_w = csv.reader(f_1)
        res = pickle.dumps(list(csv_w))
        print(res)