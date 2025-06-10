#产品
from sqlalchemy import Column, String, DECIMAL, Text, Index,Enum
from app.database import Base

class Product(Base):
    __tablename__ = "product"

    product_id = Column(String(20), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    purchase_price = Column(DECIMAL(10, 2), nullable=False)
    selling_price = Column(DECIMAL(10, 2), nullable=False)
    description = Column(Text)

    __table_args__ = (
        Index("idx_category", "category"),
    )

    status = Column(Enum('在售','下架'),default='在售')