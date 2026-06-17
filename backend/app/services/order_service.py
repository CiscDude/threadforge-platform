from sqlalchemy.orm import Session

from app.models.order import Order, OrderItem
from app.models.product import Product
from app.schemas.order import OrderCreate


def create_order(db: Session, user_id: int, order_data: OrderCreate):
    total_amount = 0.0

    for item in order_data.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            return None
        total_amount += item.unit_price * item.quantity

    order = Order(
        user_id=user_id,
        total_amount=total_amount,
        shipping_address=order_data.shipping_address,
        status="pending",
        payment_status="pending",
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    for item in order_data.items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            customization_id=item.customization_id,
            quantity=item.quantity,
            unit_price=item.unit_price,
        )
        db.add(order_item)

    db.commit()
    db.refresh(order)

    return order


def get_user_orders(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).all()


def get_order_by_id(db: Session, user_id: int, order_id: int):
    return db.query(Order).filter(Order.id == order_id, Order.user_id == user_id).first()


def update_order_status(db: Session, order_id: int, status: str):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        return None

    order.status = status

    db.commit()
    db.refresh(order)

    return order
