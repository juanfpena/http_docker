"""Selects views by year."""

import pandas as pd
from utils import engine


def view_selector(view: str) -> None:
    """Selects and displays specified view."""

    df = pd.read_sql(f'SELECT * FROM {view}_by_year;', con=engine)

    print(df)
