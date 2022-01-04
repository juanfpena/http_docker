"""Selects views by month."""

import pandas as pd
from utils import engine


def view_selector(view: str) -> None:
    """Selects and displays specified view."""

    df = pd.read_sql(f'SELECT * FROM {view}_by_month;', con=engine)

    print(df)
