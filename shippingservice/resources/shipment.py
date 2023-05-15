from datetime import datetime
from flask import jsonify

from daos.shipping_dao import ShippingDAO
from db import Session


class Shipment:
    @staticmethod
    def create(body):
        session = Session()
        shipment = ShippingDAO(body['user_id'], body['package_id'], body['status'])
        session.add(shipment)
        session.commit()
        session.refresh(shipment)
        session.close()
        return jsonify({'shipment_id': shipment.id}), 200

    @staticmethod
    def get(s_id):
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


