from app.db.connection import get_db
from app.crud import tasks, users, users2tasks 
from app.routers.schemas import TaskSchema, MutationResponse, TaskFieldsSchema

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get("/v1/tasks", response_model=List[TaskSchema])
def get_all_tasks(db: Session = Depends(get_db)):
    return tasks.get_all(db)

@router.post("/v1/tasks", response_model=MutationResponse)
def create_task(task: TaskFieldsSchema,  db: Session = Depends(get_db)):
    created_task = tasks.create(db, task)
    return { "success": True, "detail": "successfully created task", "payload": TaskSchema(**created_task.__dict__) }

@router.put("/v1/tasks/{taskId}", response_model=MutationResponse)
def update_task(taskId: int, task: TaskFieldsSchema,  db: Session = Depends(get_db)):
    found_task = tasks.get_one(db=db, id=taskId)
    if found_task is None:
        return { "success": False, "detail": "specified task does not exist" }

    updated_task = tasks.update(db, taskId=taskId, task=task)
    return { "success": True, "detail": "updated task successfully", "payload": TaskSchema(**updated_task.__dict__) }


@router.put("/v1/tasks/{taskId}/assign/user/{userId}", response_model=MutationResponse)
def assign_task_2_user(taskId: int, userId: int, db: Session = Depends(get_db)):
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

@router.put("/v1/tasks/{taskId}/unassign/user/{userId}", response_model=MutationResponse)
def unassign_task_from_user(taskId: int, userId: int, db: Session = Depends(get_db)):
    users2tasks.destroy(db, userId=userId, taskId=taskId)
    return { "success": True, "detail": "successfully unassigned task" }

@router.delete("/v1/tasks/{taskId}", response_model=MutationResponse)
def delete_task(taskId:int, db: Session = Depends(get_db)):
    tasks.destroy(db, id=taskId)
    return { "success": True, "detail": "successfully deleted task" }
