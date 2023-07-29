import csv
import json

def json_to_csv():
    with (open('file_name_id_al.json', 'r', encoding='utf-8') as f_1,
          open('new_csv.csv', 'w', newline='') as f_2):

        dict_json = json.load(f_1)
        csv_wr = csv.DictWriter(f_2, fieldnames=['name', 'id', 'access_level'])
        csv_wr.writeheader()
        for i in dict_json:
            csv_wr.writerow(i)

