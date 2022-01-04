"""Updates row in desired table."""

from sqlalchemy.sql.expression import update
from functions.update_id import update_row
import sys

if __name__ == '__main__':

    arguments = sys.argv[1:]
    update_row(arguments=arguments)
