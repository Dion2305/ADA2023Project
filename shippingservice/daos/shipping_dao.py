import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime

from db import Base


class ShippingDAO(Base):
    """ User Model for storing shipping related details """
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True)  # Auto generated primary key
    user = Column(String(255), nullable=True)
    status = Column(String(255), nullable=True)
    package_id = Column(Integer, nullable=True)


    def __init__(self, user, status, package_id):
        self.user = user
        self.status = status
        self.package_id = package_id
