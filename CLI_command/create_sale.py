"""Creates sale given arguments."""

from custom.functions.create_sale import sale_creator
import sys

arguments = sys.argv


if __name__ == '__main__':

    sale_creator(arguments=arguments)
