import os
import sys
from os import path
from faker import Faker
from faker.providers import internet, person, lorem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    sys.path.append(path.join(path.dirname(__file__), '..'))

    from models.user import User
    from models.product import Product

    DB_URL = os.getenv('DB_URL')
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    faker = Faker()
    faker.add_provider(internet)
    faker.add_provider(person)
    faker.add_provider(lorem)

    for _ in range(100):
        _user = User(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            balance=500
        )
        session.add(_user)

    for _ in range(100):
        _product = Product(
            name=f'{faker.word()} product',
            price=faker.random_int(min=0, max=999, step=1),
            stock=faker.random_int(min=0, max=999, step=1),
            discount=faker.random_int(min=0, max=9, step=1)
        )
        session.add(_product)

    session.commit()
