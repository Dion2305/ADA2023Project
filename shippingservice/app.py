from flask import Flask, request, make_response, jsonify
import os
import requests
from db import Base, engine

from resources.shipment import Shipment

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/shipments', methods=['POST'])
def create_shipment():
    req_data = request.get_json()
    return Shipment.create_shipment(req_data)


@app.route('/shipments/<s_id>', methods=['POST'])
def get_shipment(s_id):
    result = Shipment.get_user_data(s_id)
    return result


app.run(host='0.0.0.0', port=5000)
