from app.db.connection import get_db
from app.crud import users

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional 

router = APIRouter()

@router.get("/v1/users", response_model=List[dict])
def get_all_users(db: Session = Depends(get_db)):
    return users.get_all(db)
