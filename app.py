from custom.functions.create_sale import sale_creator
from custom.SQL_models import models
from sqlalchemy.orm.session import Session
from custom.SQL_models.utils import session
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import custom.SQL_models.schemas as schemas
from starlette.responses import RedirectResponse
from custom.functions.insert_into import insert_into
from fastapi.params import Depends
from fastapi import FastAPI
from sqlalchemy.sql.sqltypes import Boolean
from typing import Dict


# import pymysql
# pymysql.install_as_MySQLdb()


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


@app.get("/")
async def main():
    return RedirectResponse(url="/docs")

# GET ALL request


@app.get("/sale/select/", tags=["Sale Table"])
async def get_sale(db: Session = Depends(get_db)) -> Dict:
    sale = db.query(models.Sale).all()

    return sale


@app.get("/expense_family/select/", tags=["Expense Family Table"])
async def get_family(db: Session = Depends(get_db)) -> Dict:
    family = db.query(models.ExpenseFamily).all()

    return family


@app.get("/expense_item/select/", tags=["Expense Item Table"])
async def get_expense_item(db: Session = Depends(get_db)) -> Dict:
    expense_item = db.query(models.ExpenseItem).all()

    return expense_item


@app.get("/assigned_expense_item/select/", tags=["Assigned Expense Item Table"])
async def get_assei(db: Session = Depends(get_db)) -> Dict:
    assigned_expense_items = db.query(models.AssignedExpenseItem).all()

    return assigned_expense_items


@app.get("/purchase/select/", tags=["Purchase Table"])
async def get_purchase(db: Session = Depends(get_db)) -> Dict:
    purchase = db.query(models.Purchase).all()

    return purchase


@app.get("/customer/select/", tags=["Customer Table"])
async def get_customer(db: Session = Depends(get_db)) -> Dict:
    customer = db.query(models.Customer).all()

    return customer


@app.get("/product/select/", tags=["Product Table"])
async def get_product(db: Session = Depends(get_db)) -> Dict:
    product = db.query(models.Product).all()

    return product


@app.get("/sale_to_purchase/select/", tags=["Sale To Purchase Table"])
async def get_sale_to_pur(db: Session = Depends(get_db)) -> Dict:
    sale_to_pur = db.query(models.SaleToPurchase).all()

    return sale_to_pur

# GET ROW request


@app.get("/sale/select_row/{sale_id}/", tags=["Sale Table"])
async def get_sale_row(sale_id: int, db: Session = Depends(get_db)) -> Dict:
    sale = db.query(models.Sale).filter_by(id=sale_id).first()

    return sale


@app.get("/expense_family/select_row/{expense_family_id}/", tags=["Expense Family Table"])
async def get_family_row(expense_family_id: int, db: Session = Depends(get_db)) -> Dict:
    family = db.query(models.ExpenseFamily).filter_by(
        id=expense_family_id).first()

    return family


@app.get("/expense_item/select_row/{expense_item_id}/", tags=["Expense Item Table"])
async def get_expense_item_row(expense_item_id: int, db: Session = Depends(get_db)) -> Dict:
    expense_item = db.query(models.ExpenseItem).filter_by(
        id=expense_item_id).first()

    return expense_item


@app.get("/assigned_expense_item/select_row/{assei_id}/", tags=["Assigned Expense Item Table"])
async def get_assei_row(assei_id: int, db: Session = Depends(get_db)) -> Dict:
    assei = db.query(models.AssignedExpenseItem).filter_by(id=assei_id).first()

    return assei


@app.get("/purchase/select_row/{purchase_id}/", tags=["Purchase Table"])
async def get_purchase_row(purchase_id: int, db: Session = Depends(get_db)) -> Dict:
    purchase = db.query(models.Purchase).filter_by(id=purchase_id).first()

    return purchase


@app.get("/customer/select_row/{customer_id}/", tags=["Customer Table"])
async def get_customer_row(customer_id: int, db: Session = Depends(get_db)) -> Dict:
    customer = db.query(models.Customer).filter_by(id=customer_id).first()

    return customer


@app.get("/product/select_row/{product_id}/", tags=["Product Table"])
async def get_product_row(product_id: int, db: Session = Depends(get_db)) -> Dict:
    product = db.query(models.Product).filter_by(id=product_id).first()

    return product


@app.get("/sale_to_purchase/select_row/{stp_id}/", tags=["Sale To Purchase Table"])
async def get_sale_to_pur_row(stp_id: int, db: Session = Depends(get_db)) -> Dict:
    sale_to_pur = db.query(models.SaleToPurchase).filter_by(id=stp_id).first()

    return sale_to_pur

#GET views 

@app.get("/income/month/", tags=["Views month"])
async def get_income_by_month(db: Session = Depends (get_db)) -> Dict:
    income_by_month = db.execute("SELECT * FROM income_by_month").all()

    return income_by_month

@app.get("/expenses/month/", tags=["Views month"])
async def get_expenses_by_month(db: Session = Depends (get_db)) -> Dict:
    expenses_by_month = db.execute("SELECT * FROM expenses_by_month").all()

    return expenses_by_month

@app.get("/income_statement/month/", tags=["Views month"])
async def get_income_statement_by_month(db: Session = Depends (get_db)) -> Dict:
    income_statement_by_month = db.execute("SELECT * FROM income_statement_by_month").all()

    return income_statement_by_month

@app.get("/income/year/", tags=["Views year"])
async def get_income_statement_by_year(db: Session = Depends (get_db)) -> Dict:
    income_by_year = db.execute("SELECT * FROM income_by_year").all()

    return income_by_year

@app.get("/expenses/year/", tags=["Views year"])
async def get_expenses_by_year(db: Session = Depends (get_db)) -> Dict:
    expenses_by_year = db.execute("SELECT * FROM expenses_by_year").all()

    return expenses_by_year

@app.get("/income_statement/year/", tags=["Views year"])
async def get_income_statement_by_year(db: Session = Depends (get_db)) -> Dict:
    income_statement_by_year = db.execute("SELECT * FROM income_statement_by_year").all()

    return income_statement_by_year

@app.get("/revenue_growth/", tags=["Revenue growth"])
async def get_revenue_growth(db: Session = Depends (get_db)) -> Dict:
    revenue_growth = db.execute("SELECT * FROM revenue_growth").all()

    return revenue_growth


# POST Statements

@app.post("/sale/make_sale/", tags=["Sale Table"])
async def create_sale(sale_input: schemas.Sale) -> Dict:
    sale_creator(sale_input)

    return sale_input


@app.post("/expense_item/make_item/", tags=['Expense Item Table'])
async def create_expense_item(input: schemas.ExpenseItem) -> Dict:
    insert_into(models.ExpenseItem(item_name=input.item_name,
                                   family_id=input.family_id, cost=input.cost))
    return input


@app.post("/assigned_expense_item/make_assei/", tags=['Assigned Expense Item Table'])
async def create_assigned_expense_item(input: schemas.AssignedExpenseItem) -> Dict:
    insert_into(models.AssignedExpenseItem(
        item_id=input.item_id, state=input.state, created_at=input.created_at))

    return input


@app.post("/purchase/make_purchase/", tags=['Purchase Table'])
async def create_purchase(input: schemas.Purchase) -> Dict:
    insert_into(models.Purchase(product_id=input.product_id, quantity=input.quantity,
                                cost=input.cost, in_stock=input.in_stock, created_at=input.created_at)
                )

    return input


@app.post("/customer/make_customer/", tags=['Customer Table'])
async def create_customer(input: schemas.Customer) -> Dict:
    insert_into(models.Customer(name=input.name, surname=input.surname,
                                phone_number=input.phone_number, email=input.email))

    return input


@app.post("/product/make_product", tags=['Product Table'])
async def create_product(input: schemas.Product) -> Dict:
    insert_into(models.Product(price=input.price))

    return input


@app.post("/expense_family/make_family/", tags=["Expense Family Table"])
async def create_family(input: schemas.ExepenseFamily) -> Dict:
    insert_into(models.ExpenseFamily(service_name=input.service_name)
                )

    return input



# PUT request



@app.put("/expense_item/update/{expense_item_id}", tags=["Expense Item Table"])
async def put_expense_item_update(expense_item_id: int, inp: schemas.PutExpenseItem) -> Boolean:
    session.query(models.ExpenseItem).filter(models.ExpenseItem.id == expense_item_id).update(
        {'item_name': inp.item_name, 'family_id': inp.family_id, 'cost': inp.cost}
    )
    session.commit()

    return True


@app.put("/purchase/update/{purchase_id}", tags=["Purchase Table"])
async def put_purchase_update(purchase_id: int, inp: schemas.PutPurchase) -> Boolean:

    session.query(models.Purchase).filter(models.Purchase.id == purchase_id).update(
        {'product_id': inp.product_id, 'quantity': inp.quantity, 'cost': inp.cost,
         'in_stock': inp.in_stock, 'created_at': inp.created_at}
    )
    session.commit()
    return True


@app.put("/product/update/{product_id}", tags=["Product Table"])
async def put_product_update(product_id: int, inp: schemas.PutProduct) -> Boolean:

    session.query(models.Product).filter(
        models.Product.id == product_id).update({'price': inp.price})
    session.commit()
    return True


@app.put("/expense_family/update/{family_id}", tags=["Expense Family Table"])
async def put_expense_family_update(family_id: int, inp: schemas.PutExepenseFamily) -> Boolean:

    session.query(models.ExpenseFamily).filter(models.ExpenseFamily.id == purchase_id).update(
        {'service_name': inp.service_name})

    session.commit()
    return True


@app.put("/customer/update/{customer_id}", tags=["Customer Table"])
async def put_customer_update(customer_id: int, inp: schemas.PutCustomer) -> Boolean:

    session.query(models.Customer).filter(models.Customer.id == customer_id).update(
        {'name': inp.name, 'surname': inp.surname, 'email': inp.email, 'phone_number': inp.phone_number})

    session.commit()
    return True


@app.put("/assigned_expense_item/update/{assei_id}", tags=["Assigned Expense Item Table"])
async def put_assei_update(assei_id: int, inp: schemas.PutAssignedExpenseItem) -> Boolean:

    session.query(models.AssignedExpenseItem).filter(models.AssignedExpenseItem.id == id).update(
        {'item_id': inp.item_id, 'state': inp.state, 'created_at': inp.created_at}
    )

    session.commit()
    return True


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", host="127.0.0.1", port=8000, reload=True)
