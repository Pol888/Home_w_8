'''Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
'''
import csv
import json


def csv_to_json(initial_file_name, end_json_file_name):
    with (open(initial_file_name, 'r') as f_1,
          open(end_json_file_name, 'w', encoding='utf-8') as f_2):
        csv_read_list:list = list(csv.reader(f_1))
        csv_read_list[0].append('hash')
        headlines = csv_read_list[0]
        csv_read_list = csv_read_list[1:]
        for index in range(len(csv_read_list)):
            csv_read_list[index].append(hash(csv_read_list[index][0] + csv_read_list[index][1]))
            csv_read_list[index][0] = csv_read_list[index][0].lower()
            csv_read_list[index][1] = csv_read_list[index][1] + "0" * (10 - len(csv_read_list[index][1]))
            csv_read_list[index] = {headlines[0]: csv_read_list[index][0],
                                    headlines[1]: csv_read_list[index][1],
                                    headlines[2]: csv_read_list[index][2],
                                    headlines[3]: csv_read_list[index][3]}

        json.dump(csv_read_list, f_2, indent=2)




