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


@app.route('/shipments/<s_id>', methods=['GET'])
def get_shipment(s_id):
    req_data = request.get_json()
    return Shipment.get_shipment(s_id)
