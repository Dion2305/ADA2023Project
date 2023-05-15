from sqlalchemy import Column, String, Integer, Boolean, DateTime
import datetime

from db import Base


class PaymentDAO(Base):
    """ Payment Model for storing payment related details """
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String(255), nullable=True)
    bank = Column(String(255), nullable=True)
    date = Column(DateTime, nullable=False)
    confirmed = Column(Boolean, nullable=False, default=True)

    def __init__(self, user, bank):
        self.user = user
        self.bank = bank
        self.date = datetime.datetime.now()
        self.confirmed = True # We have not implemented a banking API
