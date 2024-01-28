from pydantic import BaseModel, Field
from datetime import datetime
from app.constants import TaskStatus

class HealthResponse(BaseModel):
    status: str

class UserFieldsSchema(BaseModel):
    username: str = Field(..., min_length=5, max_length=40) 

class UserSchema(UserFieldsSchema):
    id: int
    created_at: datetime

class TaskFieldsSchema(BaseModel):
    name: str = Field(..., min_length=5, max_length=40) 
    desc: str = Field(..., min_length=5, max_length=90) 
    status: TaskStatus 
    expires_at: datetime

    class Config:
        use_enum_values = True

class TaskSchema(TaskFieldsSchema):
    id: int
    created_at: datetime
