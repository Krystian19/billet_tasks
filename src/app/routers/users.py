from app.db.connection import get_db
from app.crud import users
from app.routers.schemas import UserSchema, TaskSchema, MutationResponse, UserFieldsSchema 

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional

router = APIRouter()

@router.get("/v1/users", response_model=List[UserSchema])
def get_all_users(db: Session = Depends(get_db)):
    return users.get_all(db)

@router.post("/v1/users", status_code=status.HTTP_201_CREATED, response_model=MutationResponse)
def create_user(user: UserFieldsSchema, db: Session = Depends(get_db)):
    found_user = users.get_one_with_username(db, user.username)

    if found_user is not None:
        return { "success": False, "detail": "provided username already exists" }

    created_user = users.create(db, user)
    return { "success": True, "detail": "successfully created user", "payload": UserSchema(**created_user.__dict__) }

@router.get("/v1/users/{userId}", response_model=Optional[UserSchema])
def get_user(userId: int, db: Session = Depends(get_db)):
    return users.get_one(db, userId)

@router.get("/v1/users/{userId}/tasks", response_model=List[TaskSchema])
def get_user_tasks(userId: int, db: Session = Depends(get_db)):
    return users.get_user_tasks(db, userId)

@router.delete("/v1/users/{userId}", response_model=MutationResponse)
def delete_user(userId: int, db: Session = Depends(get_db)):
    users.destroy(db, userId)
    return { "success": True, "detail": "successfully deleted user" }

