from datetime import datetime
from datetime import timedelta
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer, String, Boolean, Float, JSON, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    discount = Column(Integer)

    payments = relationship("Payment", back_populates="product")

    def __repr__(self):
        return "%s(id=%s, name=%s, price=%s, stock=%s, discount=%s)" % (
            self.__class__.__name__,
            self.id,
            self.name,
            self.price,
            self.stock,
            self.discount
        )
