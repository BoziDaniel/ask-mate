from flask import Flask, render_template, request
import data_manager as dm

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    """Show list of questions, sorted by the latest question on top"""
    question_path = "sample_data/question.csv"
    unordered_questions = dm.get_all_data_from_file(question_path)
    sorted_questions = dm.descending_sort_data_by_parameter(unordered_questions, 'submission_time')
    # sorted_questions_l = []
    # for dict in sorted_questions:
    #     sorted_questions_l.append(dm.find_the_key(dict, "title"))
    return render_template('list.html', sorted_questions=sorted_questions)


@app.route('/add-question.html')
def add_question():
    """Add new question to list, then redirect to /list page"""
    return render_template('add-question.html')


# @app.route('/question/<question_id>')
# def route_expand_question(question_id: int):
#

if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
