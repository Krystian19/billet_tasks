from app.db.models import User2Task 
from sqlalchemy.orm import Session

def create(db: Session, userId: int, taskId: int):
    db_user_2_task = User2Task(user_id=userId, task_id=taskId)
    db.add(db_user_2_task)
    db.commit()

def get_one(db: Session, userId: int, taskId: int):
    return db.query(User2Task).filter_by(user_id=userId, task_id=taskId).first()

def get_all(db: Session):
    return db.query(User2Task).all()

def get_all_user_task_ids(db: Session, userId: int):
    return db.query(User2Task).filter_by(user_id=userId).all()

def destroy(db: Session, userId: int, taskId: int):
    db.query(User2Task).filter_by(user_id=userId, task_id=taskId).delete()
    db.commit()
