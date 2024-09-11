from datetime import datetime
from pydantic import BaseModel


class Order(BaseModel):
    name: str
    price: int


class OrderRead(Order):
    id: int
    created_at: datetime


class OrderCreate(Order):
    pass


class OrderUpdate(Order):
    pass