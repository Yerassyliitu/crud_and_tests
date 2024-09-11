from services import OrderService
from src.repositories import OrderRepository


def order_service_factory() -> OrderService:
    return OrderService(OrderRepository())