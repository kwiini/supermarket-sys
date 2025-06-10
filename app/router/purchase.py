from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import purchase as schemas
from app.crud import purchase as crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Purchase)
def create(data: schemas.PurchaseCreate, db: Session = Depends(get_db)):
    return crud.create_purchase(db, data)

@router.get("/{purchase_id}", response_model=schemas.Purchase)
def read(purchase_id: str, db: Session = Depends(get_db)):
    result = crud.get_purchase(db, purchase_id)
    if not result:
        raise HTTPException(status_code=404, detail="采购不存在")
    return result

@router.delete("/{purchase_id}", deprecated=True)
def delete(purchase_id: str, db: Session = Depends(get_db)):
    return crud.delete_purchase(db, purchase_id)
