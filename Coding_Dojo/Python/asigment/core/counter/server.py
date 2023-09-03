from flask import Flask, render_template,session, redirect
app = Flask(__name__)

app.secret_key="Nun of visits"

@app.route('/')
def index():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session['count'] =+ 1
    return render_template("index.html")

@app.route('/reset')
def increament():
    session.clear()
    return redirect('/')


if __name__=='__Main__':
    app.run(debug=True, port=8000)