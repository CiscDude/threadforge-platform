from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    description: str | None = None
    price: float = Field(..., gt=0)
    category: str
    image_url: str | None = None
    stock_quantity: int = Field(default=0, ge=0)
    is_customizable: bool = False
    is_active: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = Field(default=None, gt=0)
    category: str | None = None
    image_url: str | None = None
    stock_quantity: int | None = Field(default=None, ge=0)
    is_customizable: bool | None = None
    is_active: bool | None = None


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
