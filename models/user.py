from datetime import datetime
from datetime import timedelta
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer, String, Boolean, Float, JSON, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    balance = Column(Integer)

    payments = relationship('Payment', back_populates='user')
    payment_tasks = relationship('PaymentTask', back_populates='user')

    def __repr__(self):
        return "%s(id=%s, fname=%s, lname=%s, email=%s, balance=%s)" % (
            self.__class__.__name__,
            self.id,
            self.first_name,
            self.last_name,
            self.email,
            self.balance
        )
