"""Creates views in the database."""

from functions.create_views import view_generator


if __name__ == "__main__":
    view_generator()
    print('Views created or updated in database.\n')
