from datetime import datetime
from flask import jsonify, make_response

from daos.shipping_dao import ShippingDAO
from db import Session


class Shipment:
    @staticmethod
    def create_shipment(post_data):
        session = Session()
        if post_data.get('status') == "payed":
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
                'message': 'Payment has not been received yet.'
            }
            return make_response(jsonify(responseObject)), 202

    @staticmethod
    def get_user_data(post_data):
        session = Session()
        id = post_data.get('user')
        if 'AUTH_URL' in os.environ:
            auth_url = os.environ['AUTH_URL']
        else:
            auth_url = 'http://accounts_ct:5000/get_user'
        result = requests.post(auth_url,
                               headers={'Content-Type': 'application/json',
                                        'Authorization': auth_header})
        status_code = result.status_code
        print(status_code)
        print(result.json())
        return [status_code, result.json()]

    @staticmethod
    def get_shipment(s_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        shipment = session.query(ShippingDAO).filter(ShippingDAO.id == s_id).first()

        if shipment:
            text_out = {
                "shipment_id:": s_id,
                "user:": shipment.user,
                "package_id": shipment.package_id,
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no shipment with id {s_id}'}), 404


