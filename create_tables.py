"""File that create tables in the database"""
from functions.create_tables import table_creator

"""Create all tables"""

if __name__ == '__main__':
    table_creator()
    print('Tables created in database.\n')
