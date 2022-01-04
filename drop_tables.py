"""Remove all tables and views."""
from functions.drop_tables import table_dropper


if __name__ == "__main__":
    table_dropper()
    print('Tables dropped from database.\n')
