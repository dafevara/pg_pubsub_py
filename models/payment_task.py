from datetime import datetime
from datetime import timedelta
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer, String, Boolean, Float, JSON
from models import Base

class PaymentTask(Base):
    __tablename__ = 'payment_tasks'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    payment_id = Column(Integer)
    tries_left = Column(Integer)
    next_try_at = Column(DateTime)
    priority = Column(Integer)
    error = Column(String)
    processing = Column(Boolean)
    context = Column(JSON)
