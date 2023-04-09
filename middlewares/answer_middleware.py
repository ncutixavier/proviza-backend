from fastapi import HTTPException, Depends
from fastapi import status
from sqlalchemy.orm import Session
import uuid

from schemas import question_schema, answer_schema
from database import get_db
from models import models

def check_answer_by_id(id:uuid.UUID, db: Session = Depends(get_db)):
    answer_to_update = db.query(models.Answer).filter(models.Answer.id == id)
    updated_answer = answer_to_update.first()

    if not updated_answer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Answer has not found')
    return answer_to_update
