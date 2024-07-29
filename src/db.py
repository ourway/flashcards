# create database connection and table for flashcards using SQLAlchemy

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Flashcard(Base):
    __tablename__ = "flashcards"
    # database is postgres

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, unique=True, nullable=False)
    answer = Column(String)
    category = Column(
        String,
        index=True,
        nullable=True,
        default="General",
        server_default="General",
        unique=False,
    )
    difficulty = Column(
        Integer,
        index=True,
        nullable=True,
        default=1,
        server_default="1",
    )

    # uniq constraint on question
    __table_args__ = (UniqueConstraint("question"),)


# we want to create a event sourcing system for flashcards
# so create a table to store events
class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, nullable=False, index=True)
    event_data = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    # events happen on Flashcard table
    flashcard_id = Column(
        Integer, ForeignKey("flashcards.id"), nullable=False, index=True
    )
    processed = Column(Boolean, nullable=False, default=False)
    # uniq constraint on event_type and event_data
    __table_args__ = (UniqueConstraint("event_type", "event_data"),)


# create postgres engine
engine = create_engine("postgresql://postgres:password@db/flashcards")
Base.metadata.create_all(engine)
