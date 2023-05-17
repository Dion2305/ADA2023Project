from datetime import datetime

from flask import jsonify

from daos.beers_dao import BeersDAO
from daos.packages_dao import PackagesDAO
from db import Session


class Packages:
    @staticmethod
    def create(body):
        session = Session()
        for beer_id in body.values():
            if not session.query(BeersDAO).filter(BeersDAO.id == beer_id).first():
                session.close()
                return jsonify({'message': f'There is no beer with id {beer_id}'}), 404
        package = PackagesDAO(body['beer_id1'], body['beer_id2'], body['beer_id3'], body['beer_id4'], body['beer_id5'], body['beer_id6'])
        session.add(package)
        session.commit()
        session.refresh(package)
        session.close()
        return jsonify({'package_id': package.id}), 200

    @staticmethod
    def get(package_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        package = session.query(PackagesDAO).filter(PackagesDAO.id == package_id).first()

        if package:
            text_out = {
                "package_id:": package.id,
                "date_created": package.date,
                "beer_id1": package.beer_id1,
                "beer_id2": package.beer_id2,
                "beer_id3": package.beer_id3,
                "beer_id4": package.beer_id4,
                "beer_id5": package.beer_id5,
                "beer_id6": package.beer_id6,
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no package with id {package_id}'}), 404

    @staticmethod
    def delete(package_id):
        session = Session()
        effected_rows = session.query(PackagesDAO).filter(PackagesDAO.id == package_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no package with id {package_id}'}), 404
        else:
            return jsonify({'message': 'The package was removed'}), 200