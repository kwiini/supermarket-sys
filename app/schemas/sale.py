from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class SaleBase(BaseModel):
    member_id: str | None = None
    sale_date: datetime
    total_amount: float
    discount_amount: float = 0
    payment_method: Literal['现金', '信用卡', '移动支付']
    employee_id: str

class SaleCreate(SaleBase):
    sale_id: str

class Sale(SaleCreate):
    class Config:
        from_attributes = True