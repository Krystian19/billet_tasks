from pydantic import BaseModel, Field
from datetime import datetime

class HealthResponse(BaseModel):
    status: str

class UserFieldsSchema(BaseModel):
    username: str = Field(..., min_length=5, max_length=40) 

class UserSchema(UserFieldsSchema):
    id: int
    created_at: datetime

