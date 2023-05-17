from sqlalchemy import Column, String, Integer, Boolean, DateTime
import datetime

from db import Base


class PackagesDAO(Base):
    """ Review Model for storing beer reviews """
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    beer_id1 = Column(Integer, nullable=True)
    beer_id2 = Column(Integer, nullable=True)
    beer_id3 = Column(Integer, nullable=True)
    beer_id4 = Column(Integer, nullable=True)
    beer_id5 = Column(Integer, nullable=True)
    beer_id6 = Column(Integer, nullable=True)

    def __init__(self, beer_id1, beer_id2, beer_id3, beer_id4, beer_id5, beer_id6):
        self.beer_id1 = beer_id1
        self.beer_id2 = beer_id2
        self.beer_id3 = beer_id3
        self.beer_id4 = beer_id4
        self.beer_id5 = beer_id5
        self.beer_id6 = beer_id6