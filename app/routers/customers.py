from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.database import engine
from app.models.customer import Customer

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("/", response_model=Customer)
def create_customer(customer: Customer):
    with Session(engine) as session:
        session.add(customer)
        session.commit()
        session.refresh(customer)
        return customer

@router.get("/", response_model=list[Customer])
def list_customers():
    with Session(engine) as session:
        customers = session.exec(select(Customer)).all()
        return customers

@router.get("/{customer_id}", response_model=Customer)
def get_customer(customer_id: int):
    with Session(engine) as session:
        customer = session.get(Customer, customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        return customer

@router.put("/{customer_id}", response_model=Customer)
def update_customer(customer_id: int, updated_customer: Customer):
    with Session(engine) as session:
        customer = session.get(Customer, customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")

        customer.name = updated_customer.name
        customer.email = updated_customer.email
        customer.phone = updated_customer.phone
        customer.address = updated_customer.address

        session.add(customer)
        session.commit()
        session.refresh(customer)
        return customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int):
    with Session(engine) as session:
        customer = session.get(Customer, customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        session.delete(customer)
        session.commit()
        return {"ok": True}
