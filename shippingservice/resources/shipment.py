from datetime import datetime
from flask import jsonify

from daos.shipping_dao import ShippingDAO
from db import Session


class Shipment:
    @staticmethod
    def create_shipment(post_data):
        session = Session()
        shipment = session.query(ShippingDAO).filter(ShippingDAO.user == authorized_user).first()
        if not shipment:
            try:
                shipment = ShippingDAO(
                    user = post_data.get('user_id'),
                    package_id = post_data.get('package_id'),
                    status = post_data.get('status'))

                session.add(shipment)
                session.commit()
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully created shipping request.',
                    'shipment_id': shipment.id
                    }
                session.close()
                return make_response(jsonify(responseObject)), 200
            except Exception as e:
                print(e)
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
                responseObject = {
                    'status': 'fail',
                    'message': 'Shipment already exists.',
                }
                return make_response(jsonify(responseObject)), 202


    @staticmethod
    def get_shipment(s_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        shipment = session.query(ShippingDAO).filter(ShippingDAO.id == s_id).first()

        if shipment:
            text_out = {
                "user_id:": shipment.user_id,
                "package_id": shipment.package_id,
                "status": shipment.status
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no shipment with id {s_id}'}), 404


