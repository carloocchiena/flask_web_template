

from flask import Flask, request
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
            errors += "<p>Attenzione! {!r} non mi sembra un numero.</p>\n".format(request.form["people"])
        try:
            budget = float(request.form["budget"])
        except:
            errors += "<p>Attenzione! {!r} non mi sembra un numero.</p>\n".format(request.form["budget"])
        if people is not None and budget is not None:
            result = virtual(people, budget)
            return '''
                <html>
                    <head>
                            <link rel="stylesheet" href="mystyle.css">
                    </head>
                    <body>
                        <h1> Ecco il tuo risultato:</h1>
                        <p> {result} </p>
                        <p><a href="/"> Vuoi fare un altro giro?</a>
                    </body>
                </html>
            '''.format(result=result)

    return '''
        <html>
            <body>
                <h1> Event Virtualize </h1>
                <h2>Crea il tuo evento online in 3 secondi!</h2>
                <p>Dammi un po' di dati:</p>
                <form method="post" action=".">
                    <p><input name="people" placeholder="Numero di partecipanti"/></p>
                    <p><input name="budget" placeholder="Budget a disposizione" /></p>
                    <p><input type="submit" value="Elabora!" /></p>
                </form>
                {errors}
            </body>
        </html>
    '''.format(errors=errors)
