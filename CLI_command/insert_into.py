"""Inserts value into desired table."""

from custom.functions.insert_into import insert_into
import sys

if __name__ == '__main__':

    arguments = sys.argv
    """Insert into the selected table, the values you want"""
    insert_into(arguments=arguments)
