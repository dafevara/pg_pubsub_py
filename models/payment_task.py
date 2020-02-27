from datetime import datetime
from datetime import timedelta
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer, String, Boolean, Float, JSON, ForeignKey
from sqlalchemy.orm import relationship
from models import Base
from sqlalchemy.orm.exc import NoResultFound
from db_session import session

class PaymentTask(Base):
    __tablename__ = 'payment_tasks'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='payment_tasks')

    payment_id = Column(Integer, ForeignKey('payments.id'))
    payment = relationship('Payment', back_populates='payment_tasks')

    tries_left = Column(Integer)
    next_try_at = Column(DateTime)
    priority = Column(Integer)
    error = Column(String)
    processing = Column(Boolean)
    context = Column(JSON)



    @classmethod
    def next(klass):
        query = """
            UPDATE %s SET
                processing = true,
                tries_left = tries_left - 1,
                error = NULL,
                next_try_at = NULL,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = (
                SELECT id
                FROM %s
                WHERE tries_left > 0
                AND (
                    next_try_at IS NULL OR
                    next_try_at < CURRENT_TIMESTAMP
                )
                AND (
                    processing = false OR
                    updated_at < CURRENT_TIMESTAMP - INTERVAL '5 SEC'
                )
                ORDER BY priority ASC, next_try_at ASC, id ASC
                FOR UPDATE SKIP LOCKED
                LIMIT 1
            )
            RETURNING *
        """ % (klass.__tablename__, klass.__tablename__)

        try:
            rs = session.execute(query).fetchone()
            session.commit()

            if rs:
                result = session.query(PaymentTask).filter_by(id=rs['id']).one()

                return result
            else:
                return None
        except NoResultFound:
            print('No task to update')

    def perform(self):
        debit = self.payment.product.price
        balance = self.user.balance
        balance -= debit

        if balance < 0:
            message = f'''
                User doesn't have enought credits.
                product price: {debit},
                current balance: {self.user.balance}
            '''

            if self.tries_left > 0:
                self.failed(message)
                print('payment failed or incomplete')
                return
        else:
            self.user.balance = balance
            try:
                session.add(self.user)
                session.commit()
                return
            except Exception as ex:
                print(str(ex))

    def destroy(self):
        try:
            session.delete(self)
            session.commit()
        except Exception as ex:
            print(str(ex))

    def failed(self, message):
        self.processing = False
        self.error = message
        self.tries_left = self.tries_left - 1
        self.next_try_at = datetime.now() + timedelta(seconds=1)

        session.add(self)
        session.commit()

    def __repr__(self):
        return "%s(id=%s, uid=%s, pay_id=%s, t_left=%s, error=%s, proc=%s)" % (
            self.__class__.__name__,
            self.id,
            self.user_id,
            self.payment_id,
            self.tries_left,
            self.error,
            self.processing
        )

