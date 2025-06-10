from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    category: str
    purchase_price: float
    selling_price: float
    description: Optional[str] = None

class ProductCreate(ProductBase):
    product_id: str

class Product(ProductCreate):
    class Config:
        orm_mode = True
