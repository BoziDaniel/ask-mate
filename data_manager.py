import csv


questions_path = "sample_data/question.csv"


def get_all_data_from_file(file_path):
    file_content = []
    with open(file_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_in_file = dict(row)
            file_content.append(row_in_file)
    return file_content   # list of dictonarys


def descending_sort_data_by_parameter(data_to_be_sorted, parameter):
    sorted_data = []
    sorted_data = sorted(data_to_be_sorted, key=lambda k: k[parameter], reverse=True)
    return sorted_data


def get_subdictionary_by_id(question_id, file_path):
    data = get_all_data_from_file(file_path)  # list of dicts
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


def get_a_column_from_data(column_name, list_of_dicts):
    items_in_column = []
    for subdict in list_of_dicts:
        items_in_column.append(subdict[column_name])
    return items_in_column


# #mind2 fv müxik, ez a 2. ra próba
# x = [{"id": 112, "name": "aga"}, {"id": 214, "name": "wzew"}, {"id": 1, "name": "awrrza"}]
# y = descending_sort_data_by_id(x)
# print(y)
# z = get_values_from_dict({"id": 112, "name": "aga"})
# print(z)
#
# print(get_a_column_from_data('title', questions_path))
