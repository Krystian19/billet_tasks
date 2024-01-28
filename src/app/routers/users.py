from app.db.connection import get_db
from app.crud import users, users2tasks, tasks
from app.routers.schemas import UserSchema, TaskSchema, MutationResponse

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get("/v1/users", response_model=List[UserSchema])
def get_all_users(db: Session = Depends(get_db)):
    return users.get_all(db)

@router.get("/v1/user/{userId}/tasks", response_model=List[TaskSchema])
def get_user_tasks(userId: int, db: Session = Depends(get_db)):
    return users.get_user_tasks(db, userId)

@router.post("/v1/user/{userId}/assign/task/{taskId}", response_model=MutationResponse)
def assign_task_2_user(userId: int, taskId: int, db: Session = Depends(get_db)):
    found_user = users.get_one(db, userId)
    if found_user is None:
        return { "success": False, "detail": "specified user does not exist" }

    found_task = tasks.get_one(db, taskId) 
    if found_task is None:
        return { "success": False, "detail": "specified task does not exist" }
    
    res = { "success": True, "detail": "successfully assigned task" }
    found_assignment = users2tasks.get_one(db, userId=userId, taskId=taskId)

    # NOTE: make sure the same task never gets assigned twice, probably it's a better
    # idea to achieve the same behavior through db constraints
    if found_assignment is None:
        return res

    users2tasks.create(db, userId=userId, taskId=taskId)
    return res

@router.delete("/v1/user/{userId}/unassign/task/{taskId}", response_model=MutationResponse)
def unassign_task_from_user(userId: int, taskId: int, db: Session = Depends(get_db)):
    users2tasks.destroy(db, userId=userId, taskId=taskId)
    return { "success": True, "detail": "successfully unassigned task" }
