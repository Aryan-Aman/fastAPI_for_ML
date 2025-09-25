from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import models
import crud
from schemas import EmployeeCreate, EmployeeUpdate, EmployeeGet
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management System")

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#endpoints
#create 
@app.post('/add_new', response_model= EmployeeGet)
def create_employee(emp: EmployeeCreate, db:Session=Depends(get_db)):
    return crud.create_employee(db=db, employee=emp)

#get all
@app.get('/employees', response_model=List[EmployeeGet])
def get_all_employees(db:Session=Depends(get_db)):
    return crud.get_employees(db=db)

#get individual
@app.get('/employee/{emp_id}', response_model=EmployeeGet)
def get_employee(emp_id:int, db:Session=Depends(get_db)):
    individual=crud.get_employee(db=db, emp_id=emp_id)
    if not individual:
        raise HTTPException(status_code=404, detail=f"Employee with id {emp_id} not found")
    return individual

#update
@app.put('/update/{emp_id}', response_model=EmployeeGet)
def update_employee(emp_id:int, employee:EmployeeUpdate, db:Session =Depends(get_db)):
    updated_emp=crud.update_employee(db=db, emp_id=emp_id, employee=employee)
    if not updated_emp:
        raise HTTPException(status_code=404, detail=f"Employee with id {emp_id} not found")
    return updated_emp

#delete
@app.delete('/delete/{emp_id}', response_model=dict) #response_model can be dict or any custom message schema
def fire_employee(emp_id:int, db:Session=Depends(get_db)):
    res= crud.delete_employee(db=db, emp_id=emp_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Employee with id {emp_id} not found")
    # return res
    return {"message": f"Employee with id {emp_id} deleted successfully"}

