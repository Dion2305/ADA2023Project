from datetime import datetime

from flask import jsonify

from daos.beers_dao import BeersDAO
from daos.reviews_dao import ReviewsDAO
from db import Session


class Beers:
    @staticmethod
    def create(body):
        session = Session()
        if session.query(BeersDAO).filter(BeersDAO.beer_name == body['beer_name']).first():
            session.close()
            return jsonify({'message': f'There is already a beer with name {body["beer_name"]}'}), 400
        beer = BeersDAO(body['beer_name'], body['country_of_origin'], body['beer_type'], body['ibu'])
        session.add(beer)
        session.commit()
        session.refresh(beer)
        session.close()
        return jsonify({'beer_id': beer.id}), 200

    @staticmethod
    def get(beer_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        beer = session.query(BeersDAO).filter(BeersDAO.id == beer_id).first()

        if beer:
            text_out = {
                "beer_id:": beer.id,
                "beer_name": beer.beer_name,
                "country_of_origin": beer.country_of_origin,
                "beer_type": beer.beer_type,
                "ibu": beer.ibu
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no beer with id {beer_id}'}), 404

    @staticmethod
    def delete(beer_id):
        session = Session()
        effected_rows = session.query(BeersDAO).filter(BeersDAO.id == beer_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no beer with id {beer_id}'}), 404
        else:
            return jsonify({'message': 'The beer instance was removed'}), 200
            