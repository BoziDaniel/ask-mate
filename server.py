from flask import Flask, render_template, request
import data_manager as dm
import connection as cn

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    """Show list of questions, sorted by the latest question on top"""
    question_path = "sample_data/question.csv"
    unordered_questions = dm.get_all_data_from_file(question_path)
    sorted_questions = dm.descending_sort_data_by_parameter(unordered_questions, 'submission_time')
    return render_template('list.html', sorted_questions=sorted_questions)


@app.route('/question/<question_id>')
def route_expand_question(question_id):
    question_path = "sample_data/question.csv"
    answer_path = "sample_data/answer.csv"
    all_questions = dm.get_all_data_from_file(question_path)
    all_answers = dm.get_all_data_from_file(answer_path)
    return render_template('question.html', question_id=question_id, answers=all_answers, questions=all_questions)


@app.route('/add-question')
def add_question():
    """Add new question to list, then redirect to /list page"""
    # cn.add_new_question()
    return render_template('add-question.html')


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
