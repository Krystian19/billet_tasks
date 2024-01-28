from fastapi import APIRouter, Path
from typing import List, Optional 

router = APIRouter()

@router.get("/v1/users", response_model=List[dict])
async def get_all_users():
    return [] 
