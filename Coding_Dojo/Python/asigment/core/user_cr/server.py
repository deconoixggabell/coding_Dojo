from flask import Flask, render_template,request, redirect
from users import user

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html", users=user.get_all())

@app.route('users/new_user')
def new_user():
    return render_template("new_user.html")

@app.route('/user/create',methods=['POST'])
def create_new_user():
    # return render_template('new_user.html')
    user.save(request.form)
    return redirect('/users')

if __name__ =='__main__':
    app.run(debug=True,port=8000)