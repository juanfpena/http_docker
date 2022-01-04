"""Deletes id from specified table."""

from functions.delete_id import delete_id
import sys

if __name__ == '__main__':

    arguments = sys.argv
    delete_id(arguments=arguments)
