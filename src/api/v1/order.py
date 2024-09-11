from typing import Annotated, List
from fastapi import APIRouter, Depends
from src.schemas import OrderRead, OrderCreate
from src.services import OrderService
from src.dependencies import order_service_factory

order_router = APIRouter("orders", prefix="/orders", tags=["orders"])


@order_router.post(
    "/", 
    response_model=OrderRead
)
async def create_order_view(
    order: OrderCreate, 
    order_service: Annotated[OrderService, Depends(order_service_factory)]
):
    return await order_service.create_entity(order)


@order_router.get(
    "/{id}", 
    response_model=OrderRead
)
async def get_order_view(
    id: int, 
    order_service: Annotated[OrderService, Depends(order_service_factory)]
):
    return await order_service.get_entity(id=id)


@order_router.get(
    "/", 
    response_model=List[OrderRead]
)
async def get_orders_view(
    order_service: Annotated[OrderService, Depends(order_service_factory)]
):
    return await order_service.get_entities()


@order_router.put(
    "/{id}", 
    response_model=OrderRead
)
async def update_order_view(
    id: int, 
    order: OrderCreate, 
    order_service: Annotated[OrderService, Depends(order_service_factory)]
):
    return await order_service.update_entity(order, id=id)


@order_router.delete(
    "/{id}", 
    response_model=OrderRead
)
async def delete_order_view(
    id: int, 
    order_service: Annotated[OrderService, Depends(order_service_factory)]
):
    return await order_service.delete_entity(id=id)

