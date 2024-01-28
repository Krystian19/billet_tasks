from app.db.models import User
from sqlalchemy.orm import Session

def create(db: Session, user: User):
    db_user = User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh()

    return db_user

def get_all(db: Session):
    return db.query(User).all()

def get_one(db: Session, id: int):
    return db.query(User).filter_by(id=id).one()

def destroy(db: Session, id: int):
    db.query(User).filter_by(id=id).delete()
    db.commit()
