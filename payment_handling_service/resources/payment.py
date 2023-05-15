from flask import make_response, jsonify

class PaymentAPI:
    @staticmethod
    def pay(post_data):
        return post_data
    # def create(post_data):
    #     session = Session()
    #     # check if user already exists
    #     user = session.query(UserDAO).filter(UserDAO.id == post_data.get('email')).first()
    #     if not user:
    #         try:
    #             user = UserDAO(
    #                 email=post_data.get('email'),
    #                 password=post_data.get('password')
    #             )
    #             # insert the user
    #             session.add(user)
    #             session.commit()
    #             # generate the auth token
    #             auth_token = encode_auth_token(user.id)
    #             responseObject = {
    #                 'status': 'success',
    #                 'message': 'Successfully registered.',
    #                 'auth_token': auth_token
    #             }
    #             session.close()
    #             return make_response(jsonify(responseObject)), 200
    #         except Exception as e:
    #             print(e)
    #             responseObject = {
    #                 'status': 'fail',
    #                 'message': 'Some error occurred. Please try again.'
    #             }
    #             return make_response(jsonify(responseObject)), 401
    #     else:
    #         responseObject = {
    #             'status': 'fail',
    #             'message': 'User already exists. Please Log in.',
    #         }
    #         return make_response(jsonify(responseObject)), 202