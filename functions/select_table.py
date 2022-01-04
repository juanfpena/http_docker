"""Defines functions for table displaying."""
"""Displays tables in CLI."""


from utils import engine
import pandas as pd
tables = [
    'sale',
    'product',
    'expense_family',
    'expense_item',
    'assigned_expense_item',
    'product',
    'purchase',
    'sale_to_purchase'
]


def show_table(table: str) -> None:
    """Returns query in pandas dataframe form."""

    df = pd.read_sql(f'SELECT * FROM {table};', con=engine)

    print(df)
