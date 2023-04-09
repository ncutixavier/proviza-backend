from fastapi import HTTPException, Depends
from fastapi import status
from sqlalchemy.orm import Session
import uuid

from schemas import question_schema, answer_schema
from database import get_db
from models import models


def check_existing_question(question: question_schema.CreateQuestionSchema, db: Session = Depends(get_db)):
    question_query = db.query(models.Question).filter(models.Question.question == question.question)
    exist_question = question_query.first()

    if exist_question:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Question called [{question.question}] already exists')
    return question


def check_question_by_id(id:uuid.UUID, db: Session = Depends(get_db)):
    question_to_update = db.query(models.Question).filter(models.Question.id == id)
    updated_question = question_to_update.first()

    if not updated_question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Question has not found')
    return question_to_update


def check_question_id_from_answer(answer: answer_schema.CreateAnswerSchema, db: Session = Depends(get_db)):
    question_to_update = db.query(models.Question).filter(models.Question.id == answer.question_id)
    updated_question = question_to_update.first()

    if not updated_question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Question has not found')
    return answer

def check_question_id_exist(question_id:uuid.UUID, db: Session = Depends(get_db)):
    question_to_update = db.query(models.Question).filter(models.Question.id == question_id)
    updated_question = question_to_update.first()

    if not updated_question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Question has not found')
    return question_id
