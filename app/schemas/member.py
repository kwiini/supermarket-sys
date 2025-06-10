from pydantic import BaseModel
from datetime import date
from typing import Literal

class MemberBase(BaseModel):
    name: str
    phone: str
    email: str | None = None
    address: str | None = None
    register_date: date
    member_type: Literal['普通', '黄金']
    expiry_date: date

class MemberCreate(MemberBase):
    member_id: str

class Member(MemberCreate):
    class Config:
        orm_mode = True