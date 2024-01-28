from app.db.connection import get_db
from app.crud import tasks 
from app.routers.schemas import TaskSchema, MutationResponse, TaskFieldsSchema

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get("/v1/tasks", response_model=List[TaskSchema])
def get_all_tasks(db: Session = Depends(get_db)):
    return tasks.get_all(db)

@router.post("/v1/tasks", status_code=status.HTTP_201_CREATED, response_model=MutationResponse)
def create_task(task: TaskFieldsSchema,  db: Session = Depends(get_db)):
    created_task = tasks.create(db, task)
    return { "success": True, "detail": "successfully created task", "payload": TaskSchema(**created_task.__dict__) }

@router.put("/v1/tasks/{taskId}", status_code=status.HTTP_201_CREATED, response_model=MutationResponse)
def update_task(taskId: int, task: TaskFieldsSchema,  db: Session = Depends(get_db)):
    found_task = tasks.get_one(db=db, id=taskId)
    if found_task is None:
        return { "success": False, "detail": "specified task does not exist" }

    updated_task = tasks.update(db, taskId=taskId, task=task)
    return { "success": True, "detail": "updated task successfully", "payload": TaskSchema(**updated_task.__dict__) }
