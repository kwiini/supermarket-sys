#采购
from sqlalchemy import Column,String,Integer,Date,DECIMAL,ForeignKey,Index
from app.database import Base

class Purchase(Base):
    __tablename__="purchase"

    purchase_id = Column(String(20), primary_key=True, index=True)
    supplier_id = Column(String(20), ForeignKey("supplier.supplier_id"), nullable=False)
    product_id = Column(String(20), ForeignKey("product.product_id"), nullable=False)
    purchase_date = Column(Date,nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(10,2),nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False)
    employee_id = Column(String(20), ForeignKey("employee.employee_id"), nullable=False)

    __table_args__ = (
        Index("idx_supplier_purchase", "supplier_id", "purchase_date"),
    )


