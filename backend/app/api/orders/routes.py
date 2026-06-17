from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_database
from app.schemas.order import OrderCreate, OrderResponse
from app.services.order_service import (
    create_order,
    get_order_by_id,
    get_user_orders,
    update_order_status,
)


router = APIRouter(prefix="/orders", tags=["Orders"])


TEMP_USER_ID = 1


@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_new_order(order_data: OrderCreate, db: Session = Depends(get_database)):
    order = create_order(db, TEMP_USER_ID, order_data)

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="One or more products were not found",
        )

    return order


@router.get("/", response_model=list[OrderResponse])
def list_orders(db: Session = Depends(get_database)):
    return get_user_orders(db, TEMP_USER_ID)


@router.get("/{order_id}", response_model=OrderResponse)
def retrieve_order(order_id: int, db: Session = Depends(get_database)):
    order = get_order_by_id(db, TEMP_USER_ID, order_id)

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    return order


@router.put("/{order_id}/status", response_model=OrderResponse)
def change_order_status(
    order_id: int,
    order_status: str,
    db: Session = Depends(get_database),
):
    order = update_order_status(db, order_id, order_status)

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    return order
