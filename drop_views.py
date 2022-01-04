"""Drops views from the database."""

from functions.drop_views import drop_all_views


if __name__ == "__main__":
    drop_all_views()
    print('Views dropped from database.\n')
