from datetime import datetime
from flask import jsonify, make_response
import requests
from daos.shipping_dao import ShippingDAO
from db import Session
import os


class Shipment:
    @staticmethod
    def create_shipment(post_data):
        session = Session()
        user = Shipment.get_user_data(post_data.get('user')).get('user')
        if ((post_data.get('status') == "payed") and (user != None)):
            shipment = ShippingDAO(
                user=post_data.get('user'),
                package_id=post_data.get('package_id'),
                status=post_data.get('status'))

            session.add(shipment)
            session.commit()
            responseObject = {
                'status': 'success',
                'message': 'Successfully created shipping request.',
                'shipment_id': shipment.id
            }
            session.close()
            return make_response(jsonify(responseObject)), 200
        # elif (user == None):
        #     responseObject = {
        #         'status': 'Failed',
        #         'message': 'No user with this id exists'
        #     }
        #     return make_response(jsonify(responseObject)), 202
        else:
            responseObject = {
                'status': 'Failed',
                'message': 'Payment has not been received yet.'
            }
            return make_response(jsonify(responseObject)), 202

    @staticmethod
    def get_user_data(s_id):
        session = Session()
        if 'AUTH_URL' in os.environ:
            auth_url = os.environ['AUTH_URL']
        else:
            auth_url = 'http://accounts_ct:5000/get_user'

        result = requests.post(url=auth_url,
                               headers={"Content-type": "application/json"},
                               json={"user": s_id})

        session.close()
        return result.json()




