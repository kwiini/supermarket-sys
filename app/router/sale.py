from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import sale as schemas
from app.crud import sale as crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Sale)
def create(data: schemas.SaleCreate, db: Session = Depends(get_db)):
    return crud.create_sale(db, data)

@router.get("/{sale_id}", response_model=schemas.Sale)
def read(sale_id: str, db: Session = Depends(get_db)):
    result = crud.get_sale(db, sale_id)
    if not result:
        raise HTTPException(status_code=404, detail="销售记录不存在")
    return result

@router.delete("/{sale_id}")
def delete(sale_id: str, db: Session = Depends(get_db)):
    return crud.delete_sale(db, sale_id)