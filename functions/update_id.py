from utils import session
from models import Product, Purchase, Customer, ExpenseItem, ExpenseFamily, AssignedExpenseItem


def update_row(arguments: list) -> None:
    """Updates row from specified table and id with provided values."""

    table_name = arguments[0]
    id = int(arguments[1])
    values = arguments[-1].split(',')

    if table_name == 'product':

        price = int(values[0])
        session.query(Product).filter(
            Product.id == id).update({'price': price})

    elif table_name == 'customer':

        name = values[0]
        surname = values[1]
        email = values[2]
        phone_number = values[3]

        session.query(Customer).filter(Customer.id == id).update(
            {'name': name, 'surname': surname, 'email': email, 'phone_number': phone_number})

    elif table_name == 'purchase':

        product_id = int(values[0])
        quantity = int(values[1])
        cost = int(values[2])
        in_stock = int(values[3])
        created_at = values[-1]

        session.query(Purchase).filter(Purchase.id == id).update(
            {'product_id': product_id, 'quantity': quantity, 'cost': cost,
                'in_stock': in_stock, 'created_at': created_at}
        )

    elif table_name == 'expense_family':

        service_name = values[0]

        session.query(ExpenseFamily).filter(ExpenseFamily.id ==
                                            id).update({'service_name': service_name})

    elif table_name == 'expense_item':

        item_name = values[0]
        family_id = int(values[1])
        cost = int(values[-1])

        session.query(ExpenseItem).filter(ExpenseItem.id == id).update(
            {'item_name': item_name, 'family_id': family_id, 'cost': cost}
        )

    elif table_name == 'assigned_expense_item':

        item_id = int(values[0])
        state = values[1]
        created_at = values[-1]

        session.query(AssignedExpenseItem).filter(AssignedExpenseItem.id == id).update(
            {'item_id': item_id, 'state': state, 'created_at': created_at}
        )

    else:
        print('table not recognized')

    session.commit()
