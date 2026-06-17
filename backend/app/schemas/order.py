from pydantic import BaseModel, Field


class OrderItemCreate(BaseModel):
    product_id: int
    customization_id: int | None = None
    quantity: int = Field(default=1, ge=1)
    unit_price: float = Field(..., gt=0)


class OrderCreate(BaseModel):
    shipping_address: str
    items: list[OrderItemCreate]


class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    customization_id: int | None
    quantity: int
    unit_price: float

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str
    payment_status: str
    shipping_address: str
    items: list[OrderItemResponse] = []

    class Config:
        from_attributes = True
