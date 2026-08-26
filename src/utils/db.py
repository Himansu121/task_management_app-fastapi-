from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.setting import settings

base = declarative_base()

engine = create_engine("postgresql://postgres:2222@localhost:5432/postgres")
session=sessionmaker(bind=engine)


def get_db():
    sessoin = session()
    try:
        yield sessoin
    finally:
        sessoin.close()       
        