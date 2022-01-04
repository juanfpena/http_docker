from utils import session
from models import Purchase, Customer, AssignedExpenseItem, ExpenseItem, ExpenseFamily, Product
from sqlalchemy import delete


def delete_id(arguments: list) -> None:
    """Deletes row from desired table using row id."""

    table_name = arguments[1]
    id = int(arguments[-1])

    tables = [
        ('product', Product),
        ('purchase', Purchase),
        ('customer', Customer),
        ('expense_item', ExpenseItem),
        ('assigned_expense_item', AssignedExpenseItem),
        ('expense_family', ExpenseFamily)]

    for name, model in tables:

        if name == table_name:
            row = session.query(model).get(id)
            session.delete(row)
            session.commit()
