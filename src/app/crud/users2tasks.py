from app.db.models import User2Task 
from sqlalchemy.orm import Session

def create(db: Session, userId: int, taskId: id):
    db_user_2_task = User2Task(userId=userId, taskId=taskId)
    db.add(db_user_2_task)
    db.commit()
    db.refresh()

    return db_user_2_task 

def get_all(db: Session):
    return db.query(User2Task).all()

def get_all_user_task_ids(db: Session, userId: int):
    return db.query(User2Task).filter_by(user_id=userId).all()
