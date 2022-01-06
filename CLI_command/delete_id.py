"""Deletes id from specified table."""

from custom.functions.delete_id import delete_id
import sys

if __name__ == '__main__':
    """Deletes row from desired table using row id."""
    arguments = sys.argv
    delete_id(arguments=arguments)
