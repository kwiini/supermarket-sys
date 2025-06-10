#销售
from sqlalchemy import Column, String, DateTime, DECIMAL, Enum, ForeignKey, Index
from app.database import Base

class Sale(Base):
    __tablename__ = "sale"

    sale_id = Column(String(20), primary_key=True, index=True)
    member_id = Column(String(20), ForeignKey("member.member_id"))
    sale_date = Column(DateTime, nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    discount_amount = Column(DECIMAL(10, 2), default=0)
    payment_method = Column(Enum("现金", "信用卡", "移动支付"), nullable=False)
    employee_id = Column(String(20), ForeignKey("employee.employee_id"), nullable=False)

    __table_args__ = (
        Index("idx_sale_date_member", "sale_date", "member_id"),
    )
