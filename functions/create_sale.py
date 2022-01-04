"""Defines sale creation function and links it to a batch utilizing FIFO exit method."""
from datetime import datetime
from logging import raiseExceptions
from types import NoneType
from models import Sale, SaleToPurchase, Purchase

from utils import session
import sys

arguments = sys.argv


def argument_parser_sales(argv: list[str]) -> list[int, str]:
    """
    Prepares sys.argv to be fed to other functions.

    Position 1: product_id
    Position 2: quantity
    Position 3: customer_id
    """

    parsed_arguments = argv[1:]
    return [int(i) for i in parsed_arguments]


def batch_iterator(quantity: int, batches: list[tuple[int]]) -> None:
    """Iterates through batches to check which ones should be modified and by what quantity."""

    batches = [list(i) for i in batches]

    used_stock = []
    modified_purchases = []

    for id, stock in batches:
        
        original_stock = stock
        
        if stock <= quantity:

            quantity -= original_stock
            stock = 0
            used_stock.append((id, original_stock))
            modified_purchases.append((id, 0))
            if quantity == 0:
                break

        if stock > quantity:
            used_stock.append((id, quantity))
            modified_purchases.append((id, stock - quantity))
            quantity = 0
            break
    if quantity > 0:
        print("Not enough stock to realize the sale")
        return
    return modified_purchases, used_stock


def sale_creator(arguments: list[int, str]) -> None:
    """Registers a sale in the destination database."""
    
    product_id, quantity_to_buy, customer_id = argument_parser_sales(argv=arguments)
    created_at = datetime.now()

    batches = session.query(Purchase.id, Purchase.in_stock).filter(
        Purchase.product_id == product_id,Purchase.in_stock > 0
        ).order_by(Purchase.created_at.asc()).all()
    # Batches are returned in ascending order (filtered by created_at) for FIFO exit method.
    try:
        new_batches, used_stock = batch_iterator(
            quantity=quantity_to_buy, batches=batches)
        transaction_state = 1
    except TypeError:
        print(f"Transaction failed \n>> product_id({product_id}), quantity({quantity_to_buy}), customer_id({customer_id}), date({created_at})")
        print("\n")
        transaction_state = 0
    
    if transaction_state == 1:
        """Gets batches necessary to fulfill the quantity required by the sale and modifies stock in those rows."""
        for i in range(len(new_batches)):

            session.query(Purchase).filter(
                Purchase.id == new_batches[i][0]
            ).update({"in_stock": f"{new_batches[i][1]}"})

            session.commit()

        """Creates and commits the sale table row."""
        new_sale = Sale(product_id=product_id, created_at=created_at,
                        quantity=quantity_to_buy,  customer_id=customer_id)

        session.add(new_sale)
        session.commit()

        """Creates and commits all purchases linked to the sale to the sale_to_purchase table."""
        new_sale_id = session.query(Sale.id).order_by(
            Sale.id.desc()).first()

        for purchase_id, stock_used in used_stock:
            new_sale_to_purchase = SaleToPurchase(
                sale_id=new_sale_id[0], purchase_id=purchase_id, quantity=stock_used)

            session.add(new_sale_to_purchase)
            session.commit()
