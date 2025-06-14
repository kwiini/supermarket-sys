from pydantic import BaseModel
from datetime import date

class InventoryBase(BaseModel):
    product_id: str
    batch_number: str
    production_date: date
    expiry_date: date
    quantity: int
    location: str

class InventoryCreate(InventoryBase):
    inventory_id: str

class Inventory(InventoryCreate):
    class Config:
        from_attributes = True