from http.client import HTTPException

from sqlalchemy.orm import Session
from app.models.product import Product as ProductModel
from app.schemas.product import ProductCreate

def get_product(db: Session, product_id: str):
    return db.query(ProductModel).filter(ProductModel.product_id == product_id, ProductModel.status != '下架').first()

def create_product(db: Session, product: ProductCreate):
    existing = db.query(ProductModel).filter(ProductModel.name == product.name).first()
    if existing:
        if existing.status == '下架':
            for key, value in product.dict().items():
                setattr(existing, key, value)
            existing.status = '在售'
            db.commit()
            return existing
        else:
            raise HTTPException(400, "商品不存在")

    else:
        obj = ProductModel(**product.dict())
        db.add(obj)
        db.commit()
        return obj

def delete_product(db: Session, product_id: str):
    obj = get_product(db, product_id)
    if not obj:
        raise HTTPException(404,"商品不存在")
    obj.status = '下架'
    db.commit()
    return obj

def get_all(db:Session):
    return db.query(ProductModel).filter(ProductModel.status == '在售').all()