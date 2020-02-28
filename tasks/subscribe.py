
import os
import sys
import random
import time

from os import path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.sql.expression import func
from faker import Faker
from faker.providers import internet, person, lorem
from tqdm import tqdm
from datetime import datetime
from datetime import timedelta

if __name__ == '__main__':
    sys.path.append(path.join(path.dirname(__file__), '..'))
    from models.user import User
    from models.product import Product
    from models.payment import Payment
    from models.payment_task import PaymentTask

    while True:
        print('waiting ...')
        task = PaymentTask.next()

        if not task:
            time.sleep(1)
            continue

        try:
            print('-')
            task.perform()
        except Exception as ex:
            task.failed(str(ex))

        if task.error is None or task.error == '':
            print('completed!')
            task.destroy()
