from app.constants import TaskStatus
from app.env import DATABASE_URL

from sqlalchemy import (Column, Integer, String, create_engine, DateTime, ForeignKey, Sequence)
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from sqlalchemy.orm import declarative_base
from datetime import datetime as dt
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=dt.utcnow, nullable=False)

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    desc = Column(String(100), nullable=True)
    status = Column(pgEnum(TaskStatus), default=TaskStatus.PENDING, nullable=False)
    expires_at = Column(DateTime, default=dt.utcnow, nullable=False)
    created_at = Column(DateTime, default=dt.utcnow, nullable=False)

class User2Task(Base):
    __tablename__ = 'users2tasks'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    task_id = Column(Integer, ForeignKey('tasks.id'))

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
