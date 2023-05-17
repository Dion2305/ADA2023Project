from flask import make_response, jsonify
from db import Session
from daos.payment_dao import PaymentDAO

class PaymentAPI:
    @staticmethod
    def pay(post_data, authorized_email):
        "Handles payment information and submits payment information to database"
        session = Session()
        payment = session.query(PaymentDAO).filter(PaymentDAO.user == authorized_email and PaymentDAO.confirmed == True).first()
        if not payment:
            try:
                payment = PaymentDAO(
                    user=authorized_email,
                    bank=post_data.get('bank'))
                session.add(payment)
                session.commit()
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully payed.'
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
                    'message': 'User already paid.',
                }
                return make_response(jsonify(responseObject)), 202

