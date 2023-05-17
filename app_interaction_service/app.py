import os

from flask import Flask, request
from db import Base, engine
from resources.app_beers import Beers
from resources.app_reviews import Reviews
from resources.packages import Packages

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)

@app.route('/beers', methods=['POST'])
def create_beer():
    req_data = request.get_json()
    return Beers.create(req_data)

@app.route('/beers/<beer_id>', methods=['GET'])
def get_beer(beer_id):
    return Beers.get(beer_id)

@app.route('/beers/<beer_id>', methods=['DELETE'])
def delete_beer(beer_id):
    return Beers.delete(beer_id)

@app.route('/reviews', methods=['POST'])
def create_review():
    return Reviews.create(req_data)

@app.route('/reviews/<beer_id>', methods=['GET'])
def get_reviews(beer_id):
    return Reviews.get(beer_id)

@app.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
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