from app.db.models import User
from app.crud import tasks, users2tasks

from sqlalchemy.orm import Session

def create(db: Session, user: User):
    db_user = User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_all(db: Session):
    return db.query(User).all()

def get_user_tasks(db: Session, id: int):
    userTasks = users2tasks.get_all_user_task_ids(db, id)
    taskIds = [userTask.task_id for userTask in userTasks]

    return tasks.get_all_with_ids(db, taskIds)

def get_one(db: Session, id: int):
    return db.query(User).filter_by(id=id).first()

def destroy(db: Session, id: int):
    db.query(User).filter_by(id=id).delete()
    db.commit()
