from datetime import datetime
from typing import List
import uuid
from pydantic import BaseModel
from schemas.question_schema import FilteredQuestionResponse

class AnswerBaseSchema(BaseModel):
    answer: str
    image: str
    is_correct: bool = False
    question_id: uuid.UUID | None = None

    class Config:
        orm_mode = True

class CreateAnswerSchema(AnswerBaseSchema):
    pass

class UpdateAnswerSchema(AnswerBaseSchema):
    pass

class AnswerResponse(AnswerBaseSchema):
    id: uuid.UUID
    question: FilteredQuestionResponse
    created_at: datetime
    updated_at: datetime

class ListAnswerResponse(BaseModel):
    results: int
    answers: List[AnswerResponse]
