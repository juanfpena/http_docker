"""Creates tables in the database"""
from sqlalchemy import create_engine
import SQL_models.models as models
from sqlalchemy.ext.declarative import declarative_base
import os

user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
host = os.environ.get('MYSQL_HOST')
port = os.environ.get('MYSQL_PORT')
db = os.environ.get('MYSQL_DB_NAME')

Base = declarative_base()
engine = create_engine(
    f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}'
)


def table_creator() -> None:
    Base.metadata.create_all(engine)
