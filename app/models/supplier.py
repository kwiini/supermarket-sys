#供应商
from sqlalchemy import Column,String,Boolean
from app.database import Base


class Supplier(Base):
    __tablename__="supplier"

    supplier_id = Column(String(20), primary_key=True, index=True)
    name = Column(String(100),nullable=False)
    contact_person = Column(String(50), nullable=False)
    phone = Column(String(20),nullable=False)
    email = Column(String(100))
    address = Column(String(200))
    supply_category = Column(String(100), nullable=False)

    is_active = Column(Boolean, default=True)

