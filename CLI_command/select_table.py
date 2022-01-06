"""This file selects table/s to show"""
from custom.functions.select_table import show_table
import sys


if __name__ == "__main__":

    table = sys.argv[-1]
    """
    select_tables <arg>
    arg : {
        'sale',
        'product',
        'expense_family',
        'expense_item',
        'assigned_expense_item',
        'product',
        'purchase',
        'sale_to_purchase'
    }
    """

    show_table(table)
