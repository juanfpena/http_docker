"""Creates sale given arguments."""

from custom.functions.create_sale import sale_creator
import sys

arguments = sys.argv


if __name__ == '__main__':
    """
    Prepares sys.argv to be fed to other functions.

    Position 1: product_id
    Position 2: quantity
    Position 3: customer_id
    """
    sale_creator(arguments=arguments)
