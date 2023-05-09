from flask import make_response, jsonify

from daos.user_dao import UserDAO
from db import Session
# see https://realpython.com/token-based-authentication-with-flask/
from jwtutil import encode_auth_token


class LoginAPI:
    @staticmethod
    def login(post_data):

        try:
            # fetch the user data
            session = Session()
            # check if user already exists
            user = session.query(UserDAO).filter(UserDAO.email == post_data.get('email')).first()
            session.close()
            if user:
                auth_token = encode_auth_token(user.id)
                if auth_token:
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token
                    }
                return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'There is no user.',
                }
            return make_response(jsonify(responseObject)), 404
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again2'
            }
            return make_response(jsonify(responseObject)), 500

    # def ChangePassword(post_data):
    #
    #     try:
    #         # fetch the user data
    #         session = Session()
    #         # check if user already exists
    #         user = session.query(UserDAO).filter(UserDAO.email == post_data.get('email')).first()
    #         if user.password == post_data.get('password'):
    #             user.ChangePassword(post_data.get('new_password'))
    #             responseObject = {
    #                 'status': 'success',
    #                 'message': 'Password succesfully changed.'
    #             }
    #             session.close()
    #             return make_response(jsonify(responseObject)), 200
    #         else:
    #             responseObject = {
    #                 'status': 'fail',
    #                 'message': 'Incorrect password'
    #             }
    #             session.close()
    #             return make_response(jsonify(responseObject)), 404
    #     except Exception as e:
    #         print(e)
    #         responseObject = {
    #             'status': 'fail',
    #             'message': 'Try again'
    #         }
    #         return make_response(jsonify(responseObject)), 500
class Password:
    @staticmethod
    def changepassword(post_data):

        try:
            # fetch the user data
            session = Session()
            # check if user already exists
            user = session.query(UserDAO).filter(UserDAO.email == post_data.get('email')).first()
            session.close()
            if user:
                auth_token = encode_auth_token(user.id)
                if auth_token:
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token
                    }
                return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'There is no user.',
                }
            return make_response(jsonify(responseObject)), 404
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again3',
                'error': e
            }
            return make_response(jsonify(responseObject)), 500
