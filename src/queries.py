# queries to CRUD flashcards in the database

from db import Flashcard
from models import FlashcardModel
from session import get_db


def get_flashcards():
    with get_db() as db:
        records = db.query(Flashcard).all()
        # return dict of flashcards
        return [FlashcardModel.from_orm(record).dict() for record in records]


def get_flashcard(id: int):
    with get_db() as db:
        return db.query(Flashcard).filter(Flashcard.id == id).first()


def create_flashcard(flashcard: FlashcardModel):
    """
    example curl command to create a flashcard:
    curl -X POST http://localhost:8000/flashcards -H "Content-Type: application/json" -d
    '{"question": "What is the capital of France?", "answer": "Paris", "category":
        "Geography", "difficulty": 3}'
    """
    with get_db() as db:
        record = Flashcard(**flashcard.dict())
        db.add(record)
        db.commit()
        db.refresh(record)
        # convert sqlalchemy model into pydantic model
        output = FlashcardModel.from_orm(record)
        return output.dict()


def update_flashcard(id: int, flashcard: FlashcardModel):
    with get_db() as db:
        db.query(Flashcard).filter(Flashcard.id == id).update(flashcard.dict())
        db.commit()
        return flashcard


def delete_flashcard(id: int):
    with get_db() as db:
        flashcard = db.query(Flashcard).filter(Flashcard.id == id).first()
        db.delete(flashcard)
        db.commit()
        return flashcard
