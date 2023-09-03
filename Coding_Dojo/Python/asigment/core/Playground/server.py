from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", phase="hello", times=5)

@app.route('/play')
def play_1():
    return render_template("index.html", nim=3, color="blue")

@app.route('/play/num')
def play_2(num):
    return render_template("index.html",num = num, color="blue")

@app.route('/play/num/color')
def play_3(num,color):
    return render_template("index.html", num = num, color = color)

if __name__== "__main__":
    app.run(debug = True, port=5000)