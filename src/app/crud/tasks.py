from app.db.models import Task 
from sqlalchemy.orm import Session

def create(db: Session, task: Task):
    db_task = Task(name=task.name, desc=task.desc, status=task.status, expires_at=task.expires_at)
    db.add(db_task)
    db.commit()
    db.refresh()

    return db_task

def get_all(db: Session):
    return db.query(Task).all()

def get_all(db: Session):
    return db.query(Task).all()

def get_one(db: Session, id: int):
    return db.query(Task).filter_by(id=id).one()

def destroy(db: Session, id: int):
    db.query(Task).filter_by(id=id).delete()
    db.commit()
