from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import inventory as schemas
from app.crud import inventory as crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Inventory)
def create(data: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.create_inventory(db, data)

@router.get("/{inventory_id}", response_model=schemas.Inventory)
def read(inventory_id: str, db: Session = Depends(get_db)):
    result = crud.get_inventory(db, inventory_id)
    if not result:
        raise HTTPException(status_code=404, detail="记录不存在")
    return result

@router.delete("/{inventory_id}")
def delete(inventory_id: str, db: Session = Depends(get_db)):
    return crud.delete_inventory(db, inventory_id)

@router.get("/", response_model=list[schemas.Inventory])
def getAll(db:Session = Depends(get_db)):
    return crud.get_all(db)