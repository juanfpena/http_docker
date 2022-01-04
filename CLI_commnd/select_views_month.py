"""Select and show tables views"""
from functions.select_views_month import view_selector
import sys


if __name__ == '__main__':

    view_requested = sys.argv[-1]

    view_selector(view=view_requested)
