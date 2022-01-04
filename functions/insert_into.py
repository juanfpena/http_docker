"""Inserts new row into desired table."""

from utils import session
from models import Product, Purchase, Customer, ExpenseFamily, ExpenseItem, AssignedExpenseItem


def insert_into(arguments: list) -> None:
    """Inserts a new row into desired table."""

    table_name = arguments[1]
    values = arguments[-1].split(',')

    if table_name not in ['product', 'purchase', 'customer', 'expense_item', 'assigned_expense_item', 'expense_family']:
        print('Table not recognized.\n')

    else:

        if table_name == 'product':
            price = int(values[0])

            new_row = Product(price=price)

        elif table_name == 'expense_family':
            service_name = values[0]

            new_row = ExpenseFamily(service_name=service_name)

        elif table_name == 'expense_item':
            item_name = values[0]
            family_id = int(values[1])
            cost = int(values[2])

            new_row = ExpenseItem(item_name=item_name,
                                  family_id=family_id, cost=cost)

        elif table_name == 'assigned_expense_item':
            item_id = int(values[0])
            state = values[1]
            created_at = values[2]

            new_row = AssignedExpenseItem(
                item_id=item_id, state=state, created_at=created_at)

        elif table_name == 'purchase':
            product_id = values[0]
            quantity = values[1]
            cost = values[2]
            in_stock = values[3]
            created_at = values[4]

            new_row = Purchase(product_id=product_id, quantity=quantity,
                               cost=cost, in_stock=in_stock, created_at=created_at)

        elif table_name == 'customer':
            name = values[0]
            surname = values[1]
            phone_number = values[2]
            email = values[3]

            new_row = Customer(name=name, surname=surname,
                               phone_number=phone_number, email=email)

        session.add(new_row)
        session.commit()
        print('New row added succesfully.\n')
