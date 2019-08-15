import connection as cn
import data_manager as dm


def genereate_new_id(file_path):
    sorted_questions = dm.descending_sort_data_by_parameter(
        (cn.get_all_data_from_file(file_path)), 'submission_time')
    newest_id = (sorted_questions[1])['id']
    new_id = int(newest_id)+1
    return new_id
#fura ez a new id-s fv, nem id szerint van sortolva és valamiért az 1. indexű subdict id-ját veszed utána a legnagyobbnak, nem a 0. v -1. et