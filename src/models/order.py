from datetime import datetime
from sqlalchemy import Column, DateTime, String, BigInteger, Integer
from settings import Base


class Order(Base):
    __tablename__ = "orders"
    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False) 
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)