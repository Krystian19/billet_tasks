from app.db.models import Task 
from sqlalchemy.orm import Session

def create(db: Session, task: Task):
    db_task = Task(name=task.name, desc=task.desc, status=task.status, expires_at=task.expires_at)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

def get_all(db: Session):
    return db.query(Task).all()

def get_all(db: Session):
    return db.query(Task).all()

def get_all_with_ids(db: Session, ids: list[int]):
    if len(ids) == 0:
        return []

    return db.query(Task).filter(Task.id.in_(ids)).all()

def get_one(db: Session, id: int):
    return db.query(Task).filter_by(id=id).first()

def destroy(db: Session, id: int):
    db.query(Task).filter_by(id=id).delete()
    db.commit()
