from flask import render_template,request, redirect, session, flash, Request
from flask_app import app 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User


@app.route('/')
def index():
    return redirect('/index/')

@app.route('/index/')
def reg_log():
    return render_template('index.html')

@app.route('/index/register/',methods=["POST"])
def register():
    if not User.is_valid(request.form):
        return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.add(data)
    session['user_id'] = id
    return redirect('/home/')

@app.route('/login/',methods=["POST"])
def login():
    user = User.get_email(request.form)
    if not user:
        flash("Invalid Email")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("wrong password")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/home/')

@app.route('/home/')
def home():
    if 'user_id' not in session:
        return redirect('/logout/')
    data = {
        "id":session['user_id']
    }
    return render_template("home.html", user = User.get_id(data))

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

# @app.route('/users/create/',methods=['POST'])
# def register(password):
#     data={
#         "password":password
#     }
#     confirm_password=password
#     if password == confirm_password:
#         User.add(request.form)
#         return redirect('/users')
#         flash("accout created")
#     else:
#         flash('Your password does not match')

# @app.route('/users/new_user/')
# def new_user():
#     return render_template("new_user.html")

# @app.route('/users/edit/<int:id>')
# def edit_user(id):
#     data ={
#         "id":id
#     }
#     return render_template("edit_user.html",user=User.get_one(data))

# @app.route('/users/update/',methods=['POST'])
# def update():
#     User.update(request.form)
#     return redirect('/users')

# @app.route('/users/show/<int:id>')
# def show(id):
#     data ={
#         "id":id
#     }
#     return render_template("show_user.html",user=User.get_one(data))

# @app.route('/users/delete/<int:id>')
# def delete(id):
#     data = {
#         "id":id
#     }
#     User.delete(data)
#     return redirect('/users')