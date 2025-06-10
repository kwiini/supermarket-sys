#库存
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Index
from app.database import Base

class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(String(20), primary_key=True, index=True)
    product_id = Column(String(20), ForeignKey("product.product_id"), nullable=False)
    batch_number = Column(String(50), nullable=False)
    production_date = Column(Date, nullable=False)
    expiry_date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)
    location = Column(String(100), nullable=False)

    __table_args__ = (
        Index("idx_expiry_date", "expiry_date"),
    )