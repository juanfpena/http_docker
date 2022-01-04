"""This file seed the tables with random values"""


from utils import session

import models

from functions.random_seed_generator import random_sale_creator_engine, random_customer_engine, random_purchase_engine, random_assigned_expense_item_engine, random_expense_item_engine, random_product_engine


"""Seeds database with random values used for testing purposes."""

families = [
    {
        "service_name": "marketing"
    },
    {
        "service_name": "finance"
    },
    {
        "service_name": "hr"
    },
    {
        "service_name": "others"
    }
]

expense_items = random_expense_item_engine(50, families=families)
products = random_product_engine(10)
purchases = random_purchase_engine(1000, product=products)
customers = random_customer_engine(300)

assigned_expenses = random_assigned_expense_item_engine(
    200, items=expense_items)


expense_item_seed = [
    {"class": models.ExpenseItem, "values": expense_items}]


expense_family_seed = [
    {"class": models.ExpenseFamily, "values": families}]


assigned_expense_seed = [
    {"class": models.AssignedExpenseItem, "values": assigned_expenses}]


product_seed = [{"class": models.Product, "values": products}]





purchase_seed = [{"class": models.Purchase, "values": purchases}]


customer_seed = [{"class": models.Customer, "values": customers}]


def seeder(dict_seed):
    """Using for loop to seed each table in the database"""
    for item in dict_seed:
        table_class = item["class"]
        row_to_add = []
        for value in item["values"]:
            new_row = table_class(**value)
            row_to_add.append(new_row)
        session.add_all(row_to_add)
        session.commit()


"""A list with the right order to seed the tables"""
list_of_seed = [
    product_seed,
    customer_seed,
    purchase_seed,
    expense_family_seed,
    expense_item_seed,
    assigned_expense_seed
]

if __name__ == "__main__":
    for seed in list_of_seed:
        seeder(seed)
    random_sale_creator_engine(sale_num=30, product=len(
        products), customer=len(customers))

    print('Tables seeded successfully.\n')
