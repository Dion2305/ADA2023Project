import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime

from db import Base


class ShippingDAO(Base):
    """ User Model for storing shipping related details """
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True)  # Auto generated primary key
    status = Column(String(255), nullable=False)
    package_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


    def __init__(self, status, packageId, userId):
        self.status = None
        self.package_id = None
        self.user_id = None
