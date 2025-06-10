from http.client import HTTPException

from sqlalchemy.orm import Session
from app.models.supplier import Supplier as SupplierModel
from app.schemas.supplier import SupplierCreate

def get_supplier(db:Session, supplier_id: str):
    return db.query(SupplierModel).filter(SupplierModel.supplier_id == supplier_id , SupplierModel.is_active == True).first()

def create_supplier(db: Session, supplier: SupplierCreate):
    existing = db.query(SupplierModel).filter(SupplierModel.name == supplier.name).first()
    if existing:
        if existing.is_active == False:
            for key, value in supplier.dict().items():
                setattr(existing, key, value)
            existing.is_active = True
            db.commit()
            return existing
        else:
            raise HTTPException(400,"供应商已存在")

    else:
        obj = SupplierModel(**supplier.dict())
        db.add(obj)
        db.commit()
        return obj

def delete_supplier(db: Session, supplier_id: SupplierCreate):
    obj = get_supplier(db, supplier_id)
    if not obj:
        raise HTTPException(404, "供应商不存在")
    else:
        obj.is_active = False
        db.commit()
        return obj
