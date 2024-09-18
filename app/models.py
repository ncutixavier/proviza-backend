from pydantic import BaseModel, EmailStr, constr, validator
from enum import Enum
from typing import Optional, List

class Role(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    names: constr(min_length=2)
    email: EmailStr  # Ensures email format is valid
    phone: constr(min_length=10, max_length=15)  # Ensures phone length is within the specified range
    roles: List[Role]

    @validator('roles', each_item=True)
    def validate_role(cls, role):
        if role not in Role.__members__.values():
            raise ValueError(f"Invalid role: {role}. Must be one of {list(Role)}")
        return role
    class Config:
        orm_mode = True
