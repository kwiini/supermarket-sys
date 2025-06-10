from pydantic import BaseModel

class SaleDetailBase(BaseModel):
    sale_id: str
    product_id: str
    quantity: int
    unit_price: float
    subtotal: float

class SaleDetailCreate(SaleDetailBase):
    detail_id: str

class SaleDetail(SaleDetailCreate):
    class Config:
        orm_mode = True
