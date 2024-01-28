from pydantic import BaseModel, Field
from datetime import date 

class UserFieldsSchema(BaseModel):
    username: str = Field(..., min_length=5, max_length=40) 

class UserSchema(UserFieldsSchema):
    id: int
    created_at: date

