import os

from sqlalchemy import TIMESTAMP, Column, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://username:password@localhost:5432/qorpo_database_sample")


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True)
    currency = Column(String)
    date_ = Column(TIMESTAMP)
    price = Column(Float)

    def to_dict(self):
        return {
            "id": self.id,
            "currency": self.currency,
            "date_": self.date_.isoformat(),
            "price": self.price,
        }


def init_db(connect_only=False):

    engine = create_engine(DATABASE_URL)

    if not connect_only:
        Base.metadata.create_all(engine)


def create_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()


if __name__ == "__main__":
    init_db(connect_only=False)
