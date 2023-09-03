from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/<name>')
def user_name(name):
    if name[0] == 'A' or name[0]== 'a':
        return f'welcome {name}'
    else:
        return f'Hello {name}'

@app.route('/welcome/<int:num1>/<int:num2>')
def add_num(num1, num2):
    return f'{num1 + num2}'

if __name__=="__main__":
    app.run(debug=True, port=8000)