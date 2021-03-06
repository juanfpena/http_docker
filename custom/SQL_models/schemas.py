from typing import Optional
from pydantic import BaseModel
from datetime import datetime



class Sale(BaseModel):
    id: Optional[int]
    product_id: int
    quantity: int
    customer_id: int


    class Config:
        orm_mode = True

class Purchase(BaseModel):

    id: Optional[int]
    product_id: int
    quantity: int
    cost: int
    in_stock: int
    created_at: datetime


    class Config:
        orm_mode = True

class Product(BaseModel):

    id: Optional[int]
    price: int


    class Config:
        orm_mode = True

class ExepenseFamily(BaseModel):

    id: Optional[int]
    service_name: str


    class Config:
        orm_mode = True

class Customer(BaseModel):

    id: Optional[int]
    name: str
    surname: Optional[str]
    phone_number: Optional[int]
    email: str

    class Config:
        orm_mode = True

class ExpenseItem(BaseModel):

    id: Optional[int]
    item_name: str
    family_id: int
    cost: int


    class Config:
        orm_mode = True

class AssignedExpenseItem(BaseModel):

    id: Optional[int]
    item_id: int
    state: str
    created_at: datetime


    class Config:
        orm_mode = True

class SaleToPurchase(BaseModel):

    id: Optional[int]
    sale_id: int
    purchase_id: int
    quantity: int


    class Config:
        orm_mode = True


class PutPurchase(BaseModel):

    product_id: int
    quantity: int
    cost: int
    in_stock: int
    created_at: datetime


    class Config:
        orm_mode = True

class PutProduct(BaseModel):

    price: int


    class Config:
        orm_mode = True

class PutExepenseFamily(BaseModel):

    service_name: str


    class Config:
        orm_mode = True

class PutCustomer(BaseModel):

    name: str
    surname: Optional[str]
    phone_number: Optional[int]
    email: str

    class Config:
        orm_mode = True

class PutExpenseItem(BaseModel):

    item_name: str
    family_id: int
    cost: int


    class Config:
        orm_mode = True

class PutAssignedExpenseItem(BaseModel):

    item_id: int
    state: str
    created_at: datetime


    class Config:
        orm_mode = True