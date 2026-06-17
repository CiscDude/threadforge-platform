from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_database
from app.schemas.cart import CartItemCreate, CartItemResponse, CartItemUpdate
from app.services.cart_service import (
    add_item_to_cart,
    get_cart_items,
    remove_cart_item,
    update_cart_item,
)


router = APIRouter(prefix="/cart", tags=["Cart"])


TEMP_USER_ID = 1


@router.post("/", response_model=CartItemResponse, status_code=status.HTTP_201_CREATED)
def add_to_cart(cart_data: CartItemCreate, db: Session = Depends(get_database)):
    cart_item = add_item_to_cart(db, TEMP_USER_ID, cart_data)

    if not cart_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return cart_item


@router.get("/", response_model=list[CartItemResponse])
def view_cart(db: Session = Depends(get_database)):
    return get_cart_items(db, TEMP_USER_ID)


@router.put("/{cart_item_id}", response_model=CartItemResponse)
def update_item(
    cart_item_id: int,
    cart_data: CartItemUpdate,
    db: Session = Depends(get_database),
):
    cart_item = update_cart_item(db, TEMP_USER_ID, cart_item_id, cart_data)

    if not cart_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart item not found",
        )

    return cart_item


@router.delete("/{cart_item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(cart_item_id: int, db: Session = Depends(get_database)):
    cart_item = remove_cart_item(db, TEMP_USER_ID, cart_item_id)

    if not cart_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart item not found",
        )

    return None
