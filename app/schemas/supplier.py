from pydantic import BaseModel
from datetime import date


class SupplierBase(BaseModel):
    name:str
    contact_person: str
    phone: str
    email: str | None = None
    address: str | None = None
    supply_category : str

class SupplierCreate(SupplierBase):
    supplier_id: str

class Supplier(SupplierCreate):
    class Config:
        from_attributes = True