from flask import Flask, render_template,redirect
app = Flask(__name__)

from users import users

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html", users=users.get_all())

if __name__=='__main__':
    app.run(debug=True, port=8000)