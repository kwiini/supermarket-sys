from sqlalchemy.orm import Session
from app.models.inventory import Inventory as InventoryModel
from app.schemas.inventory import InventoryCreate

def get_inventory(db: Session, inventory_id: str):
    return db.query(InventoryModel).filter(InventoryModel.inventory_id == inventory_id).first()

def create_inventory(db: Session, inventory: InventoryCreate):
    db_obj = InventoryModel(**inventory.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_inventory(db: Session, inventory_id: str):
    obj = get_inventory(db, inventory_id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj