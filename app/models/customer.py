from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]

    vehicles: List["Vehicle"] = Relationship(back_populates="customer")