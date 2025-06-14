from sqlalchemy.orm import Session
from app.models.sale_detail import SaleDetail as SaleDetailModel
from app.schemas.sale_detail import SaleDetailCreate

def get_sale_detail(db: Session, detail_id: str):
    return db.query(SaleDetailModel).filter(SaleDetailModel.detail_id == detail_id).first()

def create_sale_detail(db: Session, detail: SaleDetailCreate):
    db_obj = SaleDetailModel(**detail.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_sale_detail(db: Session, detail_id: str):
    obj = get_sale_detail(db, detail_id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj

def get_all(db:Session):
    return db.query(SaleDetailModel).all()