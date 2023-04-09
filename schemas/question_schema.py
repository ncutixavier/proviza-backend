from datetime import datetime
from typing import List
import uuid
from pydantic import BaseModel

class QuestionBaseSchema(BaseModel):
    question: str
    category: str
    
    class Config:
        orm_mode = True

class CreateQuestionSchema(QuestionBaseSchema):
    pass

class UpdateQuestionSchema(QuestionBaseSchema):
    pass

class FilteredQuestionResponse(QuestionBaseSchema):
    id: uuid.UUID

class QuestionResponse(QuestionBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

class ListQuestionResponse(BaseModel):
    page: int
    results: int
    questions: List[QuestionResponse]


