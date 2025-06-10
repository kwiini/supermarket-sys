from sqlalchemy.orm import Session
from app.models.purchase import Purchase as PurchaseModel
from app.schemas.purchase import PurchaseCreate

def get_purchase(db: Session, purchase_id: str):
    return db.query(PurchaseModel).filter(PurchaseModel.purchase_id == purchase_id).first()

def create_purchase(db: Session, purchase: PurchaseCreate):
    db_obj = PurchaseModel(**purchase.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_purchase(db: Session, purchase_id: str):
    obj = get_purchase(db, purchase_id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj