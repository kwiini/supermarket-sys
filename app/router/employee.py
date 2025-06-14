from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import employee as schemas
from app.crud import employee as crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Employee)
def create(data: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, data)

@router.get("/{employee_id}", response_model=schemas.Employee)
def read(employee_id: str, db: Session = Depends(get_db)):
    result = crud.get_employee(db, employee_id)
    if not result:
        raise HTTPException(status_code=404, detail="员工不存在")
    return result

@router.delete("/{employee_id}")
def delete(employee_id: str, db: Session = Depends(get_db)):
    return crud.delete_employee(db, employee_id)

@router.get("/", response_model=list[schemas.Employee])
def getAll(db:Session = Depends(get_db)):
    return crud.get_all(db)