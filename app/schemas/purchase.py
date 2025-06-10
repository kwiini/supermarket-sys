from pydantic import BaseModel
from datetime import date

class PurchaseBase(BaseModel):
    supplier_id: str
    product_id: str
    purchase_date: date
    quantity: int
    unit_price: float
    total_price: float
    employee_id: str

class PurchaseCreate(PurchaseBase):
    purchase_id: str

class Purchase(PurchaseCreate):
    class Config:
        orm_mode = True