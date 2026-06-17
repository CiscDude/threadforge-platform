from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_database
from app.models.order import Order
from app.models.product import Product
from app.models.user import User
from app.schemas.order import OrderResponse
from app.schemas.product import ProductResponse
from app.schemas.user import UserResponse


router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/users", response_model=list[UserResponse])
def list_all_users(skip: int = 0, limit: int = 50, db: Session = Depends(get_database)):
    return db.query(User).offset(skip).limit(limit).all()


@router.get("/products", response_model=list[ProductResponse])
def list_all_products(skip: int = 0, limit: int = 50, db: Session = Depends(get_database)):
    return db.query(Product).offset(skip).limit(limit).all()


@router.get("/orders", response_model=list[OrderResponse])
def list_all_orders(skip: int = 0, limit: int = 50, db: Session = Depends(get_database)):
    return db.query(Order).offset(skip).limit(limit).all()


@router.put("/orders/{order_id}/status", response_model=OrderResponse)
def update_admin_order_status(
    order_id: int,
    order_status: str,
    db: Session = Depends(get_database),
):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    order.status = order_status

    db.commit()
    db.refresh(order)

    return order
