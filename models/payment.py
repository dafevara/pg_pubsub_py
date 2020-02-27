from datetime import datetime
from datetime import timedelta
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer, String, Boolean, Float, JSON, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('Product', back_populates="payments")

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='payments')

    ammount = Column(Integer)

    payment_tasks = relationship('PaymentTask', back_populates='payment')

    def __repr__(self):
        return "%s(id=%s, product_id=%s, user_id=%s, ammount=%s)" % (
            self.__class__.__name__,
            self.id,
            self.product_id,
            self.user_id,
            self.ammount
        )
