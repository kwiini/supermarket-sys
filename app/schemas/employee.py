from pydantic import BaseModel
from datetime import date

class EmployeeBase(BaseModel):
    name: str
    position: str
    phone: str
    email: str | None = None
    hire_date: date
    salary: float
    manager_id: str | None = None

class EmployeeCreate(EmployeeBase):
    employee_id: str

class Employee(EmployeeCreate):
    class Config:
        orm_mode = True