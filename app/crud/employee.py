from http.client import HTTPException

from sqlalchemy.orm import Session
from app.models.employee import Employee as EmployeeModel
from app.schemas.employee import EmployeeCreate

def get_employee(db: Session, employee_id: str):
    return db.query(EmployeeModel).filter(EmployeeModel.employee_id == employee_id, EmployeeModel.is_active == True).first()

def create_employee(db: Session, employee: EmployeeCreate):
    existing = db.query(EmployeeModel).filter(EmployeeModel.name == employee.name,EmployeeModel.phone == employee.phone).first()
    if existing:
        if existing.is_active == False:
            for key, value in employee.dict().items():
                if key == "manager_id" and (value is None or str(value).upper() == "NULL"):
                    setattr(existing, key, None)
                else:
                    setattr(existing, key, value)
            existing.is_active = True
            db.commit()
            return existing
        else:
            raise HTTPException(400, "员工已存在")
    else:
        obj = EmployeeModel(**employee.dict())
        db.add(obj)
        db.commit()
        return {"message": "添加成功"}

def delete_employee(db: Session, employee_id: str):

    obj = get_employee(db, employee_id)
    if not obj:
        raise HTTPException(404,"员工不存在")
    obj.is_active = False
    db.commit()
    db.refresh(obj)
    return obj