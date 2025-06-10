from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import sale_detail as schemas
from app.crud import sale_detail as crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.SaleDetail)
def create(data: schemas.SaleDetailCreate, db: Session = Depends(get_db)):
    return crud.create_sale_detail(db, data)

@router.get("/{detail_id}", response_model=schemas.SaleDetail)
def read(detail_id: str, db: Session = Depends(get_db)):
    result = crud.get_sale_detail(db, detail_id)
    if not result:
        raise HTTPException(status_code=404, detail="销售明细不存在")
    return result

@router.delete("/{detail_id}", deprecated=True)
def delete(detail_id: str, db: Session = Depends(get_db)):
    return crud.delete_sale_detail(db, detail_id)
