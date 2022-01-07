"""This file set the connection with the database """

from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import create_engine


# user = os.environ.get('MYSQL_USER')
# host = os.environ.get('MYSQL_HOST')
# port = os.environ.get('MYSQL_PORT_NUMBER')
# db_name = os.environ.get('MYSQL_DB_NAME')

user = "root"
host = "localhost"
port = 3306
db_name = "sql_challenge"

engine = create_engine(
    f'mysql+mysqlconnector://{user}:123456@{host}:{port}/{db_name}'
)

Session = sessionmaker(engine)
session = Session()
