# pydantic model for postgres table (flashcards)

from typing import Optional

from pydantic import BaseModel


class FlashcardModel(BaseModel):
    id: Optional[int] = None
    question: str
    answer: str
    category: str
    difficulty: int

    class Config:
        from_attributes = True
