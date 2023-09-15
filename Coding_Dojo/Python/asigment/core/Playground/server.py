from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/play')

@app.route('/play')
def play_1():
    return render_template("index.html", num=3, color="blue")

@app.route('/play/<int:num>')
def play_2(num):
    return render_template("index.html",num = num, color="blue")

@app.route('/play/<int:num>/<color>')
def play_3(num,color):
    return render_template("index.html", num = num, color = color)

if __name__== "__main__":
    app.run(debug = True, port=5000)