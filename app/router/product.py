from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import product as schemas
from app.crud import product as crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Product)
def create(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.get("/{product_id}", response_model=schemas.Product)
def read(product_id: str, db: Session = Depends(get_db)):
    result = crud.get_product(db, product_id)
    if not result:
        raise HTTPException(status_code=404, detail="商品不存在")
    return result

@router.delete("/{product_id}")
def delete(product_id: str, db: Session = Depends(get_db)):
    return crud.delete_product(db, product_id)