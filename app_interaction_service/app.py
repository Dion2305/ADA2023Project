import os

from flask import Flask, request, make_response, jsonify
from db import Base, engine
from resources.app_beers import Beers
from resources.app_reviews import Reviews
from resources.packages import Packages

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)

def check_if_authorize(req):
    "Checks authorization token"
    auth_header = req.headers['Authorization']
    if 'AUTH_URL' in os.environ:
        auth_url = os.environ['AUTH_URL']
    else:
        auth_url = 'http://accounts_ct:5000/verify'
    result = requests.post(auth_url,
                           headers={'Content-Type': 'application/json',
                                    'Authorization': auth_header})
    status_code = result.status_code
    print(status_code)
    print(result.json())
    return [status_code, result.json()]

@app.route('/beers', methods=['POST'])
def create_beer():
    authorized = [200,0]#check_if_authorize(request)
    if authorized[0] != 200:
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 401
    req_data = request.get_json()
    return Beers.create(req_data)

@app.route('/beers/<beer_id>', methods=['GET'])
def get_beer(beer_id):
    return Beers.get(beer_id)

@app.route('/beers/<beer_id>', methods=['DELETE'])
def delete_beer(beer_id):
    authorized = [200,0]#check_if_authorize(request)
    if authorized[0] != 200:
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 401
    return Beers.delete(beer_id)

@app.route('/reviews', methods=['POST'])
def create_review():
    authorized = [200,0]#check_if_authorize(request)
    if authorized[0] != 200:
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 401
    req_data = request.get_json()
    return Reviews.create(req_data)

@app.route('/reviews/<beer_id>', methods=['GET'])
def get_reviews(beer_id):
    return Reviews.get(beer_id)

@app.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    authorized = [200,0]#check_if_authorize(request)
    if authorized[0] != 200:
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 401
    return Reviews.delete(review_id)

@app.route('/packages', methods=['POST'])
def create_package():
    req_data = request.get_json()
    return Packages.create(req_data)

@app.route('/packages/<package_id>', methods=['GET'])
def get_package(package_id):
    return Packages.get(package_id)

@app.route('/packages/<package_id>', methods=['DELETE'])
def delete_package(package_id):
    return Packages.delete(package_id)

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)