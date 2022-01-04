from typing import Dict
from sqlalchemy.sql.operators import op

from sqlalchemy.sql.visitors import traverse_using
from fastapi import FastAPI

from fastapi.params import Depends
from functions.insert_into import insert_into

from starlette.responses import RedirectResponse

import schemas

from fastapi.middleware.cors import CORSMiddleware

from fastapi import HTTPException

import uvicorn

from utils import session

from sqlalchemy.orm.session import Session

from SQL_models import models

from functions.create_sale import sale_creator

app = FastAPI(title="FastAPI Project",
              description="Hello World con FastAPI")


def get_db():
    try:
        db = session
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def analize(json_data):
    if type(json_data) == schemas.Sale:
        return json_data.customer_id
    else:
        return False


@app.get("/")
async def main():
    return RedirectResponse(url="/docs")

# GET ALL request


@app.get("/select/sale/", tags=["Sale Table"])
async def get_sale(db: Session = Depends(get_db)) -> Dict:
    sale = db.query(models.Sale).all()

    return sale


@app.get("/select/expense_family/", tags=["Expense Family Table"])
async def get_family_row(db: Session = Depends(get_db)) -> Dict:
    family = db.query(models.ExpenseFamily).all()

    return family


@app.get("/select/expense_item/", tags=["Expense Item Table"])
async def get_expense_item_row(db: Session = Depends(get_db)) -> Dict:
    expense_item = db.query(models.ExpenseItem).all()

    return expense_item


@app.get("/select/assigned_expense_item/", tags=["Assigned Expense Item Table"])
async def get_assei_row(db: Session = Depends(get_db)) -> Dict:
    assei = db.query(models.AssignedExpenseItem).all()

    return assei


@app.get("/select/purchase/", tags=["Purchase Table"])
async def get_purchase_row(db: Session = Depends(get_db)) -> Dict:
    purchase = db.query(models.Purchase).all()

    return purchase


@app.get("/select/customer/", tags=["Customer Table"])
async def get_customer_row(db: Session = Depends(get_db)) -> Dict:
    customer = db.query(models.Customer).all()

    return customer


@app.get("/select/product/", tags=["Product Table"])
async def get_product_row(db: Session = Depends(get_db)) -> Dict:
    product = db.query(models.Product).all()

    return product


@app.get("/select/sale_to_purchase", tags=["Sale To Purchase Table"])
async def get_sale_to_pur_row(db: Session = Depends(get_db)) -> Dict:
    sale_to_pur = db.query(models.SaleToPurchase).all()

    return sale_to_pur

# GET ROW request


@app.get("/select_row/sale/{sale_id}/", tags=["Sale Table"])
async def get_sale_row(sale_id: int, db: Session = Depends(get_db)) -> Dict:
    sale = db.query(models.Sale).filter_by(id=sale_id).first()

    return sale


@app.get("/select_row/expense_family/{expense_family_id}/", tags=["Expense Family Table"])
async def get_family_row(expense_family_id: int, db: Session = Depends(get_db)) -> Dict:
    family = db.query(models.ExpenseFamily).filter_by(
        id=expense_family_id).first()

    return family


@app.get("/select_row/expense_item/{expense_item_id}/", tags=["Expense Item Table"])
async def get_expense_item_row(expense_item_id: int, db: Session = Depends(get_db)) -> Dict:
    expense_item = db.query(models.ExpenseItem).filter_by(
        id=expense_item_id).first()

    return expense_item


@app.get("/select_row/assigned_expense_item/{assei_id}/", tags=["Assigned Expense Item Table"])
async def get_assei_row(assei_id: int, db: Session = Depends(get_db)) -> Dict:
    assei = db.query(models.AssignedExpenseItem).filter_by(id=assei_id).first()

    return assei


@app.get("/select_row/purchase/{purchase_id}/", tags=["Purchase Table"])
async def get_purchase_row(purchase_id: int, db: Session = Depends(get_db)) -> Dict:
    purchase = db.query(models.Purchase).filter_by(id=purchase_id).first()

    return purchase


@app.get("/select_row/customer/{customer_id}/", tags=["customer Table"])
async def get_customer_row(customer_id: int, db: Session = Depends(get_db)) -> Dict:
    customer = db.query(models.Customer).filter_by(id=customer_id).first()

    return customer


@app.get("/select_row/product/{product_id}/", tags=["Product Table"])
async def get_product_row(product_id: int, db: Session = Depends(get_db)) -> Dict:
    product = db.query(models.Product).filter_by(id=product_id).first()

    return product


@app.get("/select_row/sale_to_purchase/{stp_id}/", tags=["Sale To Purchase Table"])
async def get_sale_to_pur_row(stp_id: int, db: Session = Depends(get_db)) -> Dict:
    sale_to_pur = db.query(models.SaleToPurchase).filter_by(id=stp_id).first()

    return sale_to_pur


@app.post("/make_sale/sale/", tags=["Sale Table"])
async def post_sale(sale_input: schemas.Sale) -> Dict:
    sale_creator(sale_input)

    return sale_input


@app.post("/make_expense_item/expense_item/", tags=["Expense Item Table"])
async def post_sale(expense_item_inp: schemas.ExpenseItem) -> Dict:

    return sale_input


@app.post("/expense_item/{expense_item_id}/", tags=['Expense Item Table'])
async def create_expense_item(op_input: schemas.ExpenseItem) -> Dict:
    insert_into(op_input)

    return op_input


@app.post("/assigned_expense_item/{assigned_expense_item_id}/", tags=['Assigned Expense Item Table'])
async def create_assigned_expense_item(op_input: schemas.AssignedExpenseItem) -> Dict:
    insert_into(op_input)

    return op_input


@app.post("/purchase/{purchase_id}/", tags=['Purchase Table'])
async def create_purchase(op_input: schemas.Purchase) -> Dict:
    insert_into(op_input)

    return op_input


@app.post("/customer/{customer_id}/", tags=['Customer Table'])
async def create_customer(op_input: schemas.Customer) -> Dict:
    insert_into(op_input)

    return op_input


@app.post("/product/{product_id}/", tags=['Product Table'])
async def create_product(op_input: schemas.ServiceCalculator) -> Dict:
    insert_into(op_input)

    return op_input

# #PUT request
# @app.put("/sale/{sale_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}


# @app.put("/expense_family/{expense_family_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}

# @app.put("/expense_item/{expense_item_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}

# @app.put("/assigned_expense_item/{assigned_expense_item_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}


# @app.put("/purchase/{purchase_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}

# @app.put("/customer/{customer_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}

# @app.put("/product/{product_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}


# #Delete request
# @app.put("/sale/{sale_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}


# @app.put("/expense_family/{expense_family_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}

# @app.put("/expense_item/{expense_item_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}

# @app.put("/assigned_expense_item/{assigned_expense_item_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}


# @app.put("/purchase/{purchase_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}

# @app.put("/customer/{customer_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}

# @app.put("/product/{product_id}/")
# async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
#     """
#     Take a json input with 3 values:
#     arg1, agr2 and operation_type
#     then return the result in a json format
#     """
#     try:
#         operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
#     except ValueError:
#         return HTTPException(422, "Bad input")
#     return {"resul": operation_resul}

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", host="127.0.0.1", port=8000, reload=True)
