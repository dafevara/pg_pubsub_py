
import os
import sys
import random
from os import path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.sql.expression import func
from faker import Faker
from faker.providers import internet, person, lorem
from tqdm import tqdm

if __name__ == '__main__':
    sys.path.append(path.join(path.dirname(__file__), '..'))
    from models.user import User
    from models.product import Product
    from models.payment import Payment

    DB_URL = os.getenv('DB_URL')
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    iters = 10000
    faker = Faker()
    faker.add_provider(internet)
    faker.add_provider(person)
    faker.add_provider(lorem)

    with tqdm(total=iters) as progress_bar:
        for _ in range(iters):
            user = session.query(User).order_by(func.random()).first()
            product = session.query(Product).order_by(func.random()).first()
            dice = [faker.random_int(min=0, max=99, step=1), product.price]
            session.add(
                Payment(
                    user_id=user.id,
                    product_id=product.id,
                    ammount=random.choice(dice)
                )
            )
            progress_bar.update(1)

        session.commit()
