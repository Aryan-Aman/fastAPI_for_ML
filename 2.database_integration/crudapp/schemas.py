from pydantic import BaseModel, EmailStr
from typing import Optional

class EmployeeBase(BaseModel):
    name : str
    email : EmailStr
    designation : Optional[str] = None

# Input models (don't need orm_mode)
class EmployeeCreate(EmployeeBase):
    pass  # POST Request: JSON → Pydantic (EmployeeCreate) → SQLAlchemy → Database

class EmployeeUpdate(EmployeeBase):
    pass  # PUT Request: JSON → Pydantic (EmployeeUpdate) → SQLAlchemy → Database

# Output models (need from_attributes)
class EmployeeGet(EmployeeBase):
    id: int
    
    class Config:
        from_attributes = True  # GET Response: Database → SQLAlchemy → Pydantic (EmployeeGet) → JSON
                         # SQLAlchemy → Pydantic → JSON                                        # from_attributes needed here!


