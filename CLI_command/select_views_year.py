"""Select and show tables views"""
from custom.functions.select_views_year import view_selector
import sys


if __name__ == '__main__':

    view_requested = sys.argv[-1]
    """
    python select_view.py [arg1] [arg2]
    [arg1] -> "year"
    [arg2] ->{
        1   :  income_by_year
        2   :  expenses_by_year
        3   :  income_statement_by_year
    }
    """
    view_selector(view=view_requested)
