from app.constants import TaskStatus
from app.db.connection import Base, engine
from app.db.seeds import initialize_table

from sqlalchemy import (Column, Integer, String, Date, DateTime, ForeignKey)
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from sqlalchemy import event
from datetime import datetime as dt

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
    expires_at = Column(Date, default=dt.utcnow, nullable=False)
    created_at = Column(DateTime, default=dt.utcnow, nullable=False)

class User2Task(Base):
    __tablename__ = 'users2tasks'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    task_id = Column(Integer, ForeignKey('tasks.id', ondelete='CASCADE'))

# make sure to assign the table seed event right before table creation
event.listen(User.__table__, 'after_create', initialize_table)
event.listen(Task.__table__, 'after_create', initialize_table)
event.listen(User2Task.__table__, 'after_create', initialize_table)

Base.metadata.create_all(engine)
