from app.constants import TaskStatus

from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional

class HealthResponse(BaseModel):
    status: str

class MutationResponse(BaseModel):
    success: bool
    detail: Optional[str] = None
    payload: Optional[any] = None

    class Config:
        arbitrary_types_allowed = True

class UserFieldsSchema(BaseModel):
    username: str = Field(..., min_length=5, max_length=40) 

    class Config:
        orm_mode = True

class UserSchema(UserFieldsSchema):
    id: int
    created_at: datetime

class TaskFieldsSchema(BaseModel):
    name: str = Field(..., min_length=5, max_length=40) 
    desc: str = Field(..., min_length=5, max_length=90) 
    status: TaskStatus 
    expires_at: Optional[date] = None

    class Config:
        use_enum_values = True
        orm_mode = True

class TaskSchema(TaskFieldsSchema):
    id: int
    created_at: datetime
