from sqlalchemy import Column, String, Integer, Boolean, DateTime
import datetime

from db import Base


class BeersDAO(Base):
    """ Beers Model for storing beer details """
    __tablename__ = "beers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    beer_name = Column(String(255), nullable=True)
    country_of_origin = Column(String(255), nullable=True)
    beer_type = Column(String(255), nullable=False)
    ibu = Column(Integer, nullable=False, default=True)

    def __init__(self, beer_name, country_of_origin, beer_type, ibu):
        self.beer_name = beer_name
        self.country_of_origin = country_of_origin
        self.beer_type = beer_type
        self.ibu = ibu