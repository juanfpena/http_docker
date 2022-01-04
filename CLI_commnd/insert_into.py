"""Inserts value into desired table."""

from functions.insert_into import insert_into
import sys

if __name__ == '__main__':

    arguments = sys.argv
    insert_into(arguments=arguments)
