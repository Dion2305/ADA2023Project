import os

import requests
from flask import Flask, request, make_response, jsonify

from db import Base, engine
from resources.shipment import Shipment

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/shipments', methods=['POST'])
def create_shipment():
    req_data = request.get_json()
    return Shipment.create_shipment(req_data)
    # authorized = check_if_authorize(request)
    # if authorized[0] == 200:
    #     req_data = request.get_json()
    #     return Shipment.create_shipment(req_data)
    # else:
    #     responseObject = {
    #         'status': 'fail',
    #         'message': 'Try again'
    #     }
    #     return make_response(jsonify(responseObject)), 401

@app.route('/shipments/<s_id>', methods=['GET'])
def get_shipment(s_id):
    req_data = request.get_json()
    return Shipment.get_shipment(s_id)

# def get_user(req):
#     auth_header = req.headers['Authorization']
#     if 'AUTH_URL' in os.environ:
#         auth_url = os.environ['AUTH_URL']
#     else:
#         auth_url = 'http://accounts_ct:5000/verify'
#     result = requests.post(auth_url,
#                            headers={'Content-Type': 'application/json',
#                                     'Authorization': auth_header})
#     status_code = result.status_code
#     print(status_code)
#     print(result.json())
#     return [status_code, result.json()]
#
# app.run(host='0.0.0.0', port=5000, debug=True)
