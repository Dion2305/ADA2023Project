from flask import make_response, jsonify
from daos.user_dao import UserDAO
from db import Session
from jwtutil import encode_auth_token, decode_auth_token


class AccountsAPI:
    @staticmethod
    def create(post_data):
        session = Session()
        # check if user already exists
        user = session.query(UserDAO).filter(UserDAO.id == post_data.get('email')).first()
        if not user:
            try:
                user = UserDAO(
                    email=post_data.get('email'),
                    password=post_data.get('password')
                )
                # insert the user
                session.add(user)
                session.commit()
                # generate the auth token
                auth_token = encode_auth_token(user.id)
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': auth_token
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
                'message': 'User already exists. Please Log in.',
            }
            return make_response(jsonify(responseObject)), 202

    @staticmethod
    def get(auth_header):
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                session = Session()
                # check if user already exists
                user = session.query(UserDAO).filter(UserDAO.id == resp).first()
                responseObject = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'registered_on': user.registered_on
                    }
                }
                session.close()
                return make_response(jsonify(responseObject)), 200
            responseObject = {
                'status': 'fail',
                'message': resp
            }
            return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(responseObject)), 401
    @staticmethod
    def login(post_data):
        try:
            # fetch the user data
            session = Session()
            # check if user already exists
            user = session.query(UserDAO).filter(UserDAO.email == post_data.get('email')).first()
            session.close()
            if user and (user.password == post_data.get('password')):
                auth_token = encode_auth_token(user.id)
                if auth_token:
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token,
                        'password': user.password,
                        'subsciption_status': user.subscribed
                    }
                return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'There is no user/incorrect password.',
                }
            return make_response(jsonify(responseObject)), 404
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject)), 500

    def changepassword(post_data):

        try:
            # fetch the user data
            session = Session()
            # check if user already exists
            user = session.query(UserDAO).filter(UserDAO.email == post_data.get('email')).first()
            if user.password == post_data.get('password'):
                user.password = (post_data.get('new_password'))
                responseObject = {
                    'status': 'success',
                    'message': 'Password succesfully changed.',
                    'new_passowrd': user.password
                }
                session.commit()
                session.close()
                return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'Incorrect password'
                }
                session.close()
                return make_response(jsonify(responseObject)), 404
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject)), 500


    def removeaccount(post_data):

        try:
            # fetch the user data
            session = Session()
            # check if user already exists
            user = session.query(UserDAO).filter(UserDAO.email == post_data.get('email')).first()
            if user.password == post_data.get('password'):
                session.delete(user)
                responseObject = {
                    'status': 'success',
                    'message': 'Account removed succesfully.',
                }
                session.commit()
                session.close()
                return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'Incorrect username/password'
                }
                session.close()
                return make_response(jsonify(responseObject)), 404
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject)), 500


    def addshippinginformation(post_data):

        try:
            # fetch the user data
            session = Session()
            # check if user already exists
            user = session.query(UserDAO).filter(UserDAO.email == post_data.get('email')).first()
            if user.password == post_data.get('password'):
                user.address = post_data.get('address')
                user.city = post_data.get('city')
                user.zip = post_data.get('zip')
                responseObject = {
                    'status': 'success',
                    'message': 'Shipping details changed succesfully.',
                    'New Details': '{} {} {}'.format(user.address, user.city, user.zip)
                }
                session.commit()
                session.close()
                return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'Incorrect username/password'
                }
                session.close()
                return make_response(jsonify(responseObject)), 404
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again',
                'error': e
            }
            return make_response(jsonify(responseObject)), 500

    @staticmethod
    def get_user(post_data):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        user = session.query(UserDAO).filter(UserDAO.id == post_data.get('user')).first()
        if user:
            responseObject = {
                "user": user.id,
                "address": user.address,
                "city": user.city,
                "zip": user.zip
            }
            session.close()
            return make_response(jsonify(responseObject)), 200
        else:
            session.close()
            return jsonify({'message': f'There is no user with this id'}), 404

    @staticmethod
    def change_payed_status(post_data):
        session = Session()
        user = session.query(UserDAO).filter(UserDAO.email == post_data.get('email')).first()
        if user:
            user.subscribed = True
            session.commit()
            responseObject = {
                "message": "payed status succesfully changed"
            }
            session.close()
            return make_response(jsonify(responseObject)), 200
        else:
            session.close()
            return jsonify({'message': f'There is no user with this email'}), 404