"""Create tables through models with SQLAlchemy."""
from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime


from sqlalchemy.sql.schema import CheckConstraint, ForeignKey
from utils import Base


class Product(Base):
    """Stores different products, along relevant attributes for further accountability."""
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False, unique=False)


class ExpenseFamily(Base):
    """Stores different categories applied to products to help taxonomize expenses."""
    __tablename__ = "expense_family"

    id = Column(Integer, primary_key=True)
    service_name = Column(String(225), nullable=False, unique=False)


class Purchase(Base):
    """Store purchase cost and stock"""
    __tablename__ = "purchase"
    __table_args__ = (CheckConstraint("in_stock >= 0"),)

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer)
    cost = Column(Integer)
    in_stock = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())


class Sale(Base):
    """Stores sales with their given specifications."""
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    created_at = Column(DateTime, default=datetime.now())
    quantity = Column(Integer)
    customer_id = Column(Integer, ForeignKey("customer.id"))


class Customer(Base):
    """Stores user data from customer"""
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    name = Column(String(224), nullable=False, unique=False)
    surname = Column(String(224), nullable=True, unique=False)
    phone_number = Column(Integer, nullable=True, unique=True)
    email = Column(String(224), nullable=False, unique=True)


class ExpenseItem(Base):
    """Stores expense items that will later be referred to in assigned_expense_items."""
    __tablename__ = "expense_item"
    __table_args__ = (CheckConstraint("cost >= 0.0"),)

    id = Column(Integer, primary_key=True)
    item_name = Column(String(225), nullable=False, unique=True)
    family_id = Column(Integer, ForeignKey(
        "expense_family.id"), nullable=False)
    cost = Column(Float, nullable=False)


class AssignedExpenseItem(Base):
    """Stores a record of expense items, along a sales_id if expense was directly related to a sale."""
    __tablename__ = "assigned_expense_item"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("expense_item.id"))
    state = Column(String(224))
    created_at = Column(DateTime, default=datetime.now())


class SaleToPurchase(Base):
    """Stores ids_purchases for each sale_id"""
    __tablename__ = "sale_to_purchase"

    id = Column(Integer, primary_key=True)
    sale_id = Column(Integer, ForeignKey("sale.id"))
    purchase_id = Column(Integer, ForeignKey("purchase.id"))
    quantity = Column(Integer)
