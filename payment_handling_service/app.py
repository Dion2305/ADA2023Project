from flask import Flask, request, make_response, jsonify
from resources.payment import PaymentAPI
import os
import requests
from db import Base, engine

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/pay', methods=['POST'])
def pay():
    "Pay function with authorization function and sends post request for user.subscribed change to account api"
    authorized = check_if_authorize(request)
    if 'PAY_URL' in os.environ:
        pay_url = os.environ['PAY_URL']
    else:
        pay_url = 'http://accounts-ct:5000/pay_url'
    if authorized[0] == 200:
        req_data = request.get_json()
        requests.post(pay_url,
                      headers={'Content-Type': 'application/json'},
                      json={'email': authorized[1]['data']['email']})
        return PaymentAPI.pay(req_data, authorized[1]['data']['email'])
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 401


def check_if_authorize(req):
    "Checks authorization token"
    auth_header = req.headers['Authorization']
    if 'AUTH_URL' in os.environ:
        auth_url = os.environ['AUTH_URL']
    else:
        auth_url = 'http://accounts-ct:5000/verify'
    result = requests.post(auth_url,
                           headers={'Content-Type': 'application/json',
                                    'Authorization': auth_header})
    status_code = result.status_code
    print(status_code)
    print(result.json())
    return [status_code, result.json()]




app.run(host='0.0.0.0', port=5000)