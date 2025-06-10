#会员
from sqlalchemy import Column, String, Date, Enum, Index
from app.database import Base

class Member(Base):
    __tablename__ = "member"

    member_id = Column(String(20), primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100))
    address = Column(String(200))
    register_date = Column(Date, nullable=False)
    member_type = Column(Enum("普通", "黄金"), nullable=False, default="普通")
    expiry_date = Column(Date, nullable=False)

    __table_args__ = (
        Index("idx_member_type_expiry", "member_type", "expiry_date"),
    )
