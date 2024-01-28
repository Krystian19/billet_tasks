from app.db.connection import get_db
from app.crud import users
from app.routers.schemas import UserSchema, TaskSchema, MutationResponse

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get("/v1/users", response_model=List[UserSchema])
def get_all_users(db: Session = Depends(get_db)):
    return users.get_all(db)

@router.get("/v1/users/{userId}/tasks", response_model=List[TaskSchema])
def get_user_tasks(userId: int, db: Session = Depends(get_db)):
    return users.get_user_tasks(db, userId)

@router.delete("/v1/users/{userId}", response_model=MutationResponse)
def delete_user(userId: int, db: Session = Depends(get_db)):
    users.destroy(db, userId)
    return { "success": True, "detail": "successfully deleted user" }

