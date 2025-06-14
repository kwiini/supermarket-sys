from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing_extensions import deprecated

from app.schemas import member as schemas
from app.crud import member as crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Member)
def create(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.create_member(db, member)

@router.get("/{member_id}", response_model=schemas.Member)
def read(member_id: str, db: Session = Depends(get_db)):
    result = crud.get_member(db, member_id)
    if not result:
        raise HTTPException(status_code=404, detail="会员不存在")
    return result

@router.delete("/{member_id}", deprecated=True)
def delete(member_id: str, db: Session = Depends(get_db)):
    return crud.delete_member(db, member_id)

@router.get("/", response_model=list[schemas.Member])
def getAll(db:Session = Depends(get_db)):
    return crud.get_all(db)