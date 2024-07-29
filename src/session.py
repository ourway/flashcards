# context manager for database session (with get_db() as db:)
from contextlib import contextmanager

from sqlalchemy.orm import Session

from db import engine


@contextmanager
def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()
