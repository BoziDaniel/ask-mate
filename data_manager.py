import csv



questions_path = "sample_data/question.csv"


def get_all_data_from_file(file_path):
    file_content = []
    with open(file_path, encoding='utf-8') as csvfile:
        #  use DictReader to directly create dictionaries from each lines in the csv file
        reader = csv.DictReader(csvfile)
        #  read all lines in csv file
        for row in reader:
            #  make a copy of the read row, since we can't modify it
            row_in_file = dict(row)
            #  store modified data in temporary list
            file_content.append(row_in_file)
    return file_content


def descending_sort_data_by_id(data):#át lehet írni a fv-t bármire ami szám, akk kell neki még1 paraméter.
    sorted_data = []
    for i in range(len(data)):
        max_id = data[0]['id']
        max_id_element = None
        for element in data:
            if element['id'] >= max_id:
                max_id = element['id']
                max_id_element = element
        sorted_data.append(max_id_element)
        data.remove(max_id_element)
    return sorted_data


#mind2 fv müxik, ez a 2. ra próba
x = [{"id": 112, "name": "aga"}, {"id": 214, "name": "wzew"}, {"id": 1, "name": "awrrza"}]
y = descending_sort_data_by_id(x)
print(y)
