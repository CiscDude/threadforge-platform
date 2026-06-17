from pydantic import BaseModel, Field


class CartItemCreate(BaseModel):
    product_id: int
    customization_id: int | None = None
    quantity: int = Field(default=1, ge=1)


class CartItemUpdate(BaseModel):
    quantity: int = Field(..., ge=1)


class CartItemResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    customization_id: int | None
    quantity: int

    class Config:
        from_attributes = True
