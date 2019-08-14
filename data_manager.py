import csv



questions_path = "sample_data/question.csv"


def get_all_data_from_file(file_path):
    file_content = []
    with open(file_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_in_file = dict(row)
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


def get_subdictionary_by_id(question_id, file_path):
    data = get_all_data_from_file(file_path) #list of dicts
    filtered_data = []
    for element in data:
        if question_id in element.values():
            filtered_data.append(element)
    return filtered_data


def get_values_from_dict(dict_data):
    values_of_a_dict = []
    for key in dict_data:
        values_of_a_dict.append(dict_data[key])
    return values_of_a_dict


"""
#mind2 fv müxik, ez a 2. ra próba
x = [{"id": 112, "name": "aga"}, {"id": 214, "name": "wzew"}, {"id": 1, "name": "awrrza"}]
y = descending_sort_data_by_id(x)
print(y)
z = get_values_from_dict({"id": 112, "name": "aga"})
print(z)
"""