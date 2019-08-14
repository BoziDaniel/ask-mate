from flask import Flask, render_template, request
import data_manager as dm

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    question_path = "sample_data/question.csv"
    unordered_answers = dm.get_all_data_from_file(question_path)
    sorted_lines = dm.descending_sort_data_by_id(unordered_answers)
    sorted_questions = []
    for line in sorted_lines:
        sorted_questions.append(line["message"])
    return render_template('list.html', sorted_questions=sorted_questions),


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
