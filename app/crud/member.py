from sqlalchemy.orm import Session
from app.models.member import Member as MemberModel
from app.schemas.member import MemberCreate

def get_member(db: Session, member_id: str):
    return db.query(MemberModel).filter(MemberModel.member_id == member_id).first()

def create_member(db: Session, member: MemberCreate):
    db_obj = MemberModel(**member.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_member(db: Session, member_id: str):
    db_obj = get_member(db, member_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

def get_all(db:Session):
    return db.query(MemberModel).all()