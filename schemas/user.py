from datetime import datetime
from typing import List
import uuid
from pydantic import BaseModel, EmailStr, constr

class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True
    
    class Config:
        orm_mode = True

class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=6)
    role: str = 'user'

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=6)

class UserResponseSchema(UserBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
