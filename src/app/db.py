from sqlalchemy import (Column, Integer, String, create_engine, DateTime, ForeignKey)
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from datetime import datetime as dt
from sqlalchemy.orm import declarative_base
from app.constants import DATABASE_URL, TaskStatus

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column("id", Integer, primary_key=True),
    username = Column("username", String(50), nullable=False, unique=True),
    created_at = Column("created_at", DateTime, default=dt.utcnow, nullable=False),

class Task(Base):
    __tablename__ = 'tasks'

    id = Column("id", Integer, primary_key=True),
    name = Column("name", String(50), nullable=False),
    desc = Column("desc", String(100), nullable=True),
    status = Column("status", pgEnum(TaskStatus), default=TaskStatus.PENDING, nullable=False),
    expires_at = Column("expires_at", DateTime, default=dt.utcnow, nullable=False),
    created_at = Column("created_at", DateTime, default=dt.utcnow, nullable=False),

class User2Task(Base):
    __tablename__ = 'users2tasks'

    id = Column("id", Integer, primary_key=True),
    user_id = Column(Integer(), ForeignKey('users.id'))
    task_id = Column(Integer(), ForeignKey('tasks.id'))

Base.metadata.create_all(engine)
