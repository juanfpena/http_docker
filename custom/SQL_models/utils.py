"""This file set the connection with the database """

from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import create_engine


user = os.environ.get('MYSQL_USER')
host = os.environ.get('MYSQL_HOST')
port = os.environ.get('MYSQL_PORT_NUMBER')
db_name = os.environ.get('MYSQL_DB_NAME')



engine = create_engine(
    f'mysql+mysqlconnector://{user}:@{host}:{port}/{db_name}'
)

Session = sessionmaker(engine)
session = Session()
