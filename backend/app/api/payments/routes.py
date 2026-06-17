from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_database
from app.services.payment_service import (
    create_mock_payment_intent,
    get_payment_status,
    mark_order_as_paid,
)


router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/{order_id}/intent")
def create_payment_intent(order_id: int, db: Session = Depends(get_database)):
    payment_intent = create_mock_payment_intent(db, order_id)

    if not payment_intent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    return payment_intent


@router.post("/{order_id}/confirm")
def confirm_payment(order_id: int, db: Session = Depends(get_database)):
    order = mark_order_as_paid(db, order_id)

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    return {
        "message": "Payment confirmed successfully",
        "order_id": order.id,
        "payment_status": order.payment_status,
        "order_status": order.status,
    }


@router.get("/{order_id}/status")
def retrieve_payment_status(order_id: int, db: Session = Depends(get_database)):
    payment_status = get_payment_status(db, order_id)

    if not payment_status:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    return payment_status
