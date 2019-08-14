def add_new_question():
    title = request.form["title"]
    message = request.form["message"]
    values = (title, message)

    return redirect("/question/", values)
