from app.db.database import SessionLocal
from sqlalchemy.orm import Session
from contextlib import contextmanager

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()