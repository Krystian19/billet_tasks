from app.constants import TaskStatus
from app.env import DATABASE_URL

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from datetime import datetime as dt
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
