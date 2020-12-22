from flask import Flask, request, render_template
from processing import virtual

app = Flask(__name__)
app.config["DEBUG"] = True

#This decorator specifies that the following function defines what happens when someone goes to the location “/” on your site – eg. if they go to http://yourusername.pythonanywhere.com/. If you wanted to define what happens when they go to http://yourusername.pythonanywhere.com/foo then you’d use @app.route('/foo') instead.
@app.route('/', methods = ["GET", "POST"])
def input_page():
    errors = ""
    if request.method == "POST":
        people = None
        budget = None
        try:
            people = float(request.form["people"])
        except:
            errors += "Attenzione! {!r} non mi sembra un numero.\n".format(request.form["people"])
        try:
            budget = float(request.form["budget"])
        except:
            errors += "Attenzione! {!r} non mi sembra un numero.\n".format(request.form["budget"])
        if people is not None and budget is not None:
            result = virtual(people, budget)
            return render_template("results.html", result=result)

    return render_template("main.html", errors=errors)


app.run(use_reloader=False)
