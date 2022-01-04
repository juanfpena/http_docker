"""This file selects table/s to show"""
from functions.select_table import show_table
import sys


if __name__ == "__main__":

    table = sys.argv[-1]

    show_table(table)
