"""This file set the connection with the database """
import mysql.connector

from sqlalchemy.orm import sessionmaker
import os


user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
host = os.environ.get('MYSQL_HOST')
port = os.environ.get('MYSQL_PORT')
db_name = os.environ.get('MYSQL_DB_NAME')


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

Session = sessionmaker(engine)
session = Session()
