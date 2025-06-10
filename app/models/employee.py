#员工
from sqlalchemy import Column, String, Date, DECIMAL, ForeignKey, Boolean
from app.database import Base


class Employee(Base):
    __tablename__ = "employee"

    employee_id = Column(String(20),primary_key=True,index=True)
    name = Column(String(50), nullable=False)
    position = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100))
    hire_date = Column(Date, nullable=False)
    salary = Column(DECIMAL(10, 2), nullable=False)
    manager_id = Column(String(20), ForeignKey("employee.employee_id"))

    is_active = Column(Boolean,default=True)

