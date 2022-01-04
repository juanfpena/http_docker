"""This file set the connection with the database """

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

import mysql.connector

from sqlalchemy.orm import sessionmaker


user = 'root'
password = "root2021"
host = 'localhost'
port = '3306'
db_name = 'sql_challenge'


def db_creator(database_name):
    my_db = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password
    )
    my_cursor = my_db.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))
    return database_name


db = db_creator(db_name)

engine = create_engine(
    f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}'
)

Base = declarative_base()

Session = sessionmaker(engine)
session = Session()
