from app.db.connection import get_db
from app.crud import tasks 
from app.routers.schemas import TaskSchema 

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional 

router = APIRouter()

@router.get("/v1/tasks", response_model=List[TaskSchema])
def get_all_users(db: Session = Depends(get_db)):
    return tasks.get_all(db)
