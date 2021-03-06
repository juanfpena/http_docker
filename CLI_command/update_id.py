"""Updates row in desired table."""

from sqlalchemy.sql.expression import update
from custom.functions.update_id import update_row
import sys

if __name__ == '__main__':

    arguments = sys.argv[1:]
    
    """Updates row from specified table and id with provided values."""

    update_row(arguments=arguments)
