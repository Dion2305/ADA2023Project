from flask import Flask, request

from db import Base, engine
from resources.accountapi import AccountsAPI

app = Flask(__name__)
app.config["DEBUG"] = True

Base.metadata.create_all(engine)


@app.route('/register', methods=['POST'])
def register():
    req_data = request.get_json()
    return AccountsAPI.create(req_data)


@app.route('/login', methods=['POST'])
def login():
    req_data = request.get_json()
    return AccountsAPI.login(req_data)


@app.route('/verify', methods=['POST'])
def verify():
    # get the auth token
    auth_header = request.headers.get('Authorization')
    return AccountsAPI.get(auth_header)


@app.route('/changepassword', methods=['POST'])
def changepassword():
    # Changes the password
    req_data = request.get_json()
    return AccountsAPI.changepassword(req_data)


@app.route('/removeaccount', methods=['POST'])
def removeaccount():
    # Changes the password
    req_data = request.get_json()
    return AccountsAPI.removeaccount(req_data)


@app.route('/addshippinginformation', methods=['POST'])
def addshippinginformation():
    # Changes the password
    req_data = request.get_json()
    return AccountsAPI.addshippinginformation(req_data)

@app.route('/get_user', methods=['POST'])
def getuser():
    # get the auth token
    req_data = request.get_json()
    return AccountsAPI.get_user(req_data)

app.run(host='0.0.0.0', port=5000)
