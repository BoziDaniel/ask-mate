from flask import Flask, render_template, request, redirect
import data_manager as dm
import connection as cn
import util as ut
import time

app = Flask(__name__)

question_path = "sample_data/question.csv"
answer_path = "sample_data/answer.csv"


@app.route('/')
@app.route('/list', methods=['POST', 'GET'])
def route_list():
    """Show list of questions, sorted by the latest question on top"""
    unordered_questions = cn.get_all_data_from_file(question_path)
    sorted_questions = dm.descending_sort_data_by_parameter(unordered_questions, 'submission_time')
    return render_template('list.html', sorted_questions=sorted_questions)


@app.route('/question/<question_id>', methods=['POST', 'GET'])
def route_expand_question(question_id):
    all_questions = cn.get_all_data_from_file(question_path)
    all_answers = cn.get_all_data_from_file(answer_path)
    return render_template('question.html', question_id=question_id, answers=all_answers, questions=all_questions)


@app.route('/add-question', methods=['POST', 'GET'])
def add_question():
    """Add new question to list, then redirect to /list page"""
    if request.method == 'POST':
        id = ut.genereate_new_id(question_path)
        submission_time = int(time.time())
        view_number = 0
        vote_number = 0
        title = request.form["title"]
        message = request.form["message"]
        image = 0
        new_question = [id, submission_time, view_number, vote_number, title, message, image]
        cn.add_new_question(question_path, new_question)
        return redirect("/list")
    else:
        return render_template('add-question.html')


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
