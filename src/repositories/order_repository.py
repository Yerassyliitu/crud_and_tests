from src.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.models import Order

class OrderRepository(SQLAlchemyRepository):
    model = Order