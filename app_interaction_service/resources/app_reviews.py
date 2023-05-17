from datetime import datetime

from flask import jsonify

from daos.beers_dao import BeersDAO
from daos.reviews_dao import ReviewsDAO
from db import Session


class Reviews:
    @staticmethod
    def create(body):
        session = Session()
        beer_id = body['beer_id']
        if not session.query(ReviewsDAO).filter(BeersDAO.id == beer_id).first():
            session.close()
            return jsonify({'message': f'There is no beer with id {beer_id}'}), 404
        review = ReviewsDAO(body['beer_id'], body['user'], body['date'], body['rating'], body['review'])
        session.add(review)
        session.commit()
        session.refresh(review)
        session.close()
        return jsonify({'review_id': review.id}), 200
    
    @staticmethod
    def get(beer_id):
        session = Session()
        beer_reviews = session.query(ReviewsDAO).filter(ReviewsDAO.beer_id == beer_id).all()
        if beer_reviews:
            output = {}
            ratings = []
            for beer_review in beer_reviews:
                text_out = {
                    "review_id:": beer_review.id,
                    "beer_id": beer_review.beer_id,
                    "user": beer_review.user,
                    "date": beer_review.date,
                    "rating": beer_review.rating,
                    "review": beer_review.review
                }
                output[beer_review.id] = text_out
                ratings.append(beer_review.rating)
            output['average_rating'] = sum(ratings) / len(ratings)
            session.close()
            return jsonify(output), 200
        else:
            session.close()
            return jsonify({'message': f'There is no beer with id {beer_id}'}), 404

    @staticmethod
    def delete(review_id):
        session = Session()
        effected_rows = session.query(ReviewsDAO).filter(ReviewsDAO.id == review_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no review with id {review_id}'}), 404
        else:
            return jsonify({'message': 'The review was removed'}), 200