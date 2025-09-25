from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models import Employee
from schemas import EmployeeCreate, EmployeeUpdate, EmployeeGet

#Get employees
def get_employees(db: Session):
    return db.query(Employee).all()

#Get employee by id
def get_employee(db: Session, emp_id: int):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with id {emp_id} not found")
    return emp

#Create employee
def create_employee(db: Session, employee: EmployeeCreate):
    db_emp = Employee(
        name = employee.name,
        email = employee.email,
        designation = employee.designation
    )
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

#Update employee
def update_employee(db: Session, emp_id: int, employee: EmployeeUpdate):
    db_emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not db_emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with id {emp_id} not found")
    
    db_emp.name = employee.name
    db_emp.email = employee.email
    db_emp.designation = employee.designation
    
    db.commit()
    db.refresh(db_emp)
    return db_emp

#Delete employee
def delete_employee(db: Session, emp_id: int):
    db_emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not db_emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with id {emp_id} not found")
    
    db.delete(db_emp)
    db.commit()
    return {"detail": f"Employee with id {emp_id} deleted successfully"}
