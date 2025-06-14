from sqlalchemy.orm import Session
from app.models.sale import Sale as SaleModel
from app.schemas.sale import SaleCreate

def get_sale(db: Session, sale_id: str):
    return db.query(SaleModel).filter(SaleModel.sale_id == sale_id).first()

def create_sale(db: Session, sale: SaleCreate):
    db_obj = SaleModel(**sale.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_sale(db: Session, sale_id: str):
    obj = get_sale(db, sale_id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj

def get_all(db:Session):
    return db.query(SaleModel).all()