from datetime import datetime
from flask import jsonify, make_response
import requests
from daos.shipping_dao import ShippingDAO
from db import Session
import os


class Shipment:
    #Function that creates a new shipment
    @staticmethod
    def create_shipment(post_data):
        session = Session()
        user = Shipment.get_user_data(post_data.get('user')).get('user')
        package = Shipment.get_beer_data(post_data.get('package_id')).get('package_id')
        if user == post_data.get('user'): #Check if user exists
            if post_data.get('status') == "payed":  # Check if the user payed
                if package == post_data.get('package_id'):
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
                else:
                    responseObject = {
                        'status': 'Failed',
                        'message': 'No package with this id exists.'
                    }
                    return make_response(jsonify(responseObject)), 202

            else:
                responseObject = {
                    'status': 'Failed',
                    'message': 'Payment has not been received yet.'
                }
                return make_response(jsonify(responseObject)), 202
        else:
            responseObject = {
                'status': 'Failed',
                'message': 'No user with this id exists'
            }
            return make_response(jsonify(responseObject)), 202

    #Function that get the user data from the account service
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


    #Function that get the beer data from the beer service
    @staticmethod
    def get_beer_data(package_id):
        session = Session()
        if 'BEER_URL' in os.environ:
            beer_url = os.environ['BEER_URL']
        else:
            beer_url = 'http://appinteraction_ct:5003/packages/' + package_id

        result = requests.post(url=auth_url,
                               headers={"Content-type": "application/json"})

        session.close()
        return result.json()



