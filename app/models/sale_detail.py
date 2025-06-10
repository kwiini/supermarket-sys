#销售明细
from sqlalchemy import Column, String, Integer, DECIMAL, ForeignKey
from app.database import Base

class SaleDetail(Base):
    __tablename__ = "saledetail"

    detail_id = Column(String(20), primary_key=True, index=True)
    sale_id = Column(String(20), ForeignKey("sale.sale_id"), nullable=False)
    product_id = Column(String(20), ForeignKey("product.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(10, 2), nullable=False)
    subtotal = Column(DECIMAL(10, 2), nullable=False)