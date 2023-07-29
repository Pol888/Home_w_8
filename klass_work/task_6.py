'''Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.'''
import csv
import pickle


def pickle_to_csv():
    with (open('task_4_json_file.pickle', 'rb') as f_1,
          open('task_4_json_file.csv', 'w', newline='') as f_2):
        obj = pickle.load(f_1)
        csv_w = csv.DictWriter(f_2, fieldnames=["name", "id", "access_level", "hash"])
        csv_w.writeheader()
        csv_w.writerows(obj)


