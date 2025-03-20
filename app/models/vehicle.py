from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import date
from app.models.customer import Customer #relation

class Vehicle(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    license_plate: str
    brand: str
    model: str
    year: int
    customer_id: int = Field(foreign_key="customer.id")

    customer: Optional[Customer] = Relationship(back_populates="vehicles")

    # Opcional, se quiseres usar relationships
    # customer: Optional["Customer"] = Relationship(back_populates="vehicles")
