from models.order import Order
from schemas.order import OrderRead


def order_mapper(order: Order) -> OrderRead:
    return OrderRead(
        id=order.id,
        name=order.name,
        price=order.price,
        created_at=order.created_at
    )


