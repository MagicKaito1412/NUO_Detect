from . import service
from run import app
from flask import request


@app.route('/login', methods=['POST'])
def login():
    login_name = request.form.get('login')
    password = request.form.get('password')
    service.login(login_name, password)


@app.route('/logout', methods=['POST'])
def logout():
    service.logout()

