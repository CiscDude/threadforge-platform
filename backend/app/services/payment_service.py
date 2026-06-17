from sqlalchemy.orm import Session

from app.models.order import Order


def create_mock_payment_intent(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        return None

    return {
        "order_id": order.id,
        "amount": order.total_amount,
        "currency": "gbp",
        "payment_status": order.payment_status,
        "client_secret": f"mock_payment_secret_order_{order.id}",
    }


def mark_order_as_paid(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        return None

    order.payment_status = "paid"
    order.status = "confirmed"

    db.commit()
    db.refresh(order)

    return order


def get_payment_status(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        return None

    return {
        "order_id": order.id,
        "payment_status": order.payment_status,
        "order_status": order.status,
        "amount": order.total_amount,
    }
