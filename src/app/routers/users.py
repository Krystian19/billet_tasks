from app.db.connection import get_db
from app.crud import users
from app.routers.schemas import UserSchema, TaskSchema

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional 

router = APIRouter()

@router.get("/v1/users", response_model=List[UserSchema])
def get_all_users(db: Session = Depends(get_db)):
    return users.get_all(db)

@router.get("/v1/user/{userId}/tasks", response_model=List[TaskSchema])
def get_all_users(userId: int, db: Session = Depends(get_db)):
    return users.get_user_tasks(db, userId)
