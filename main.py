from flask import Flask, redirect, render_template, request, url_for
from function.newAcc import newAcc
from function.login import _login, _logout
from function.isLogin import isLogin
from function.handelMovie import _addMovie, _delMovie, _editMovie, _getAllMovie

app = Flask(__name__)


@app.route('/<string:user>')
def welcome_view(user):
    if not isLogin(user):
        return 'Not Found 404'

    return render_template('index.html', user=user, movies=_getAllMovie())


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


@app.route('/logout', methods=['POST'])
def logout():
    user = request.get_json()
    _logout(user['user'])
    return redirect(url_for('login'))


@app.route('/movie', methods=['POST', 'DELETE', 'PUT'])
def newMovie():
    if request.method == 'POST':
        data = request.get_json()
        _addMovie(data)
        return redirect(url_for('welcome_view', user="f"))
    if request.method == 'DELETE':
        data = request.get_json()
        _delMovie(data)
        return {'msg': 'ok'}
    if request.method == 'PUT':
        data = request.get_json()
        _editMovie(data)
        return {'msg': 'ok'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
