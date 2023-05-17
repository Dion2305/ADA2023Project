from sqlalchemy import Column, String, Integer, Boolean, DateTime
import datetime

from db import Base


class ReviewsDAO(Base):
    """ Review Model for storing beer reviews """
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    beer_id = Column(Integer, nullable=True)
    user = Column(String(255), nullable=True)
    rating = Column(Integer, nullable=True)
    review = Column(String(1023), nullable=True)

    def __init__(self, beer_id, user, rating, review):
        self.beer_id = beer_id
        self.user = user
        self.rating = rating
        self.review = review