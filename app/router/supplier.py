from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import supplier as schemas
from app.crud import supplier as crud
from app.database import get_db

router = APIRouter()

@router.get("/{supplier_id}",response_model=schemas.Supplier)
def read(supplier_id:str, db:Session=Depends(get_db)):
    res = crud.get_supplier(db, supplier_id)
    if not res:
        raise HTTPException(status_code=404, detail="记录不存在")
    return res

@router.post("/",response_model=schemas.Supplier)
def create(data:schemas.SupplierCreate, db:Session = Depends((get_db))):
    return crud.create_supplier(db, data)

@router.delete("/{supplier_id}")
def delete(supplier_id:str, db:Session = Depends((get_db))):
    return crud.delete_supplier(db, supplier_id)

@router.get("/", response_model=list[schemas.Supplier])
def getAll(db:Session = Depends(get_db)):
    return crud.get_all(db)