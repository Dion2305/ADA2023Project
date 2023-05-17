import os

from flask import Flask, request, render_template, jsonify
from db import Base, engine
from resources.app_beers import Beers
from resources.app_reviews import Reviews
import json

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)

# @app.route('/', methods = ['GET'])
# def home():
#     return render_template('index.html')

# @app.route('/beerexplorer', methods = ['GET'])
# def beerexplorer():
#     return render_template('beerexplorer.html')

# @app.route('/beermanager', methods = ['GET'])
# def beermanager():
#     return render_template('beermanager.html')

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
    req_data = request.get_json()
    return Reviews.create(req_data)

@app.route('/reviews/<beer_id>', methods=['GET'])
def get_reviews(beer_id):
    return Reviews.get(beer_id)

@app.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    return Reviews.delete(review_id)

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)