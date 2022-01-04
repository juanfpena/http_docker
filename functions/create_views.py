"""Creates views in database using statements in '.sql' files"""
from utils import engine
import models

income_statement_by_month = "SQL_views/income_statement_by_month.sql"
income_statement_by_year = "SQL_views/income_statement_by_year.sql"
# revenue_evolution = "SQL_views/revenue_growth.sql"

views_list = [income_statement_by_month,
              income_statement_by_year]


def sql_parser(file_path: str) -> list[str]:
    """Takes .sql file and returns a list of statements in it."""
    statements = open(file_path).read()
    statement_list = []

    for statement in statements.split('#'):
        corrected = statement.replace('\n', ' ')
        statement_list.append(corrected)

    return statement_list


def view_generator() -> None:
    """Creates or updates views inside the dbrm."""
    with engine.connect() as conn:
        for i in views_list:
            view_name = i.split('/')[-1].replace('.sql', '')
            print(f'...creating or updating view for {view_name}.')
            for s in sql_parser(i):
                conn.execute(s)
            print(f'{view_name} view created or updated successfully.')
