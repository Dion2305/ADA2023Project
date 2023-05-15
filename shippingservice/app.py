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
    if check_if_authorize(request) == 200:
        req_data = request.get_json()
        return Shipment.create(req_data)
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 401


@app.route('/shipments/<s_id>', methods=['GET'])
def get_shipment(d_id):
    if check_if_authorize(request) == 200:
        return Shipment.get(s_id)
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 401

app.run(host='0.0.0.0', port=5000, debug=True)
