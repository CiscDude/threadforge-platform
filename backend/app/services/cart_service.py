from sqlalchemy.orm import Session

from app.models.cart import CartItem
from app.models.product import Product
from app.schemas.cart import CartItemCreate, CartItemUpdate


def add_item_to_cart(db: Session, user_id: int, cart_data: CartItemCreate):
    product = db.query(Product).filter(Product.id == cart_data.product_id).first()

    if not product:
        return None

    existing_item = (
        db.query(CartItem)
        .filter(
            CartItem.user_id == user_id,
            CartItem.product_id == cart_data.product_id,
            CartItem.customization_id == cart_data.customization_id,
        )
        .first()
    )

    if existing_item:
        existing_item.quantity += cart_data.quantity
        db.commit()
        db.refresh(existing_item)
        return existing_item

    cart_item = CartItem(
        user_id=user_id,
        product_id=cart_data.product_id,
        customization_id=cart_data.customization_id,
        quantity=cart_data.quantity,
    )

    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)

    return cart_item


def get_cart_items(db: Session, user_id: int):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()


def update_cart_item(db: Session, user_id: int, cart_item_id: int, cart_data: CartItemUpdate):
    cart_item = (
        db.query(CartItem)
        .filter(CartItem.id == cart_item_id, CartItem.user_id == user_id)
        .first()
    )

    if not cart_item:
        return None

    cart_item.quantity = cart_data.quantity

    db.commit()
    db.refresh(cart_item)

    return cart_item


def remove_cart_item(db: Session, user_id: int, cart_item_id: int):
    cart_item = (
        db.query(CartItem)
        .filter(CartItem.id == cart_item_id, CartItem.user_id == user_id)
        .first()
    )

    if not cart_item:
        return None

    db.delete(cart_item)
    db.commit()

    return cart_item
