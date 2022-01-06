"""Select and show tables views"""
from custom.functions.select_views_month import view_selector
import sys


if __name__ == '__main__':

    view_requested = sys.argv[-1]
    """
    python select_view.py [arg1] [arg2]
    [arg1] -> "month"
    [arg2] ->{
        1   :  income_by_month / income_by_year
        2   :  expenses_by_month / expenses_by_year
        3   :  income_statement_by_month /
    }
    """

    view_selector(view=view_requested)
