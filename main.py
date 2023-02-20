from flask import Flask, redirect, render_template, request, url_for
from function.newAcc import newAcc
from function.login import _login
from function.isLogin import isLogin

app = Flask(__name__)


@app.route('/<string:user>')
def welcome_view(user):
    if not isLogin(user):
        return 'Not Found 404'
    return render_template('index.html', user=user)


@app.route('/sum/<int:first_num>/<int:second_num>')
def sum_two(first_num, second_num):
    total = first_num + second_num
    return 'The sum of {} and {} is: {}'.format(first_num, second_num, total)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        usr = request.form.get('usr')
        psw = request.form.get('psw')
        if _login(usr, psw):
            return redirect(url_for('welcome_view', user=usr))
        else:
            return redirect('/login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        usr = request.form.get('usr')
        psw = request.form.get('psw')
        # check new account
        if newAcc(usr, psw):
            return f'New account with <br/> username: <b>{usr}</b> <br/> password: <b>{psw}</b>'
        else:
            return f'Username: <b>{usr}</b> is already!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
