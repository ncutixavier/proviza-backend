import uuid
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from schemas import question_schema
from database import get_db
from models.models import Question
from middlewares import question_middleware

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=question_schema.QuestionResponse)
def create_question(question: question_schema.CreateQuestionSchema = Depends(question_middleware.check_existing_question), 
                    db: Session = Depends(get_db)):
    new_question = Question(**question.dict())
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question


@router.get('/', status_code=status.HTTP_200_OK, response_model=question_schema.ListQuestionResponse)
def get_questions(db: Session = Depends(get_db), limit: int=10, page: int=1, search: str = ''):
    skip = (page-1) * limit
    questions = db.query(Question).group_by(Question.id).filter(
        Question.question.contains(search)).limit(limit).offset(skip).all()
    return {'page': page, 'results': len(questions), 'questions': questions}


@router.get('/{id}', response_model=question_schema.QuestionResponse)
def get_question(id:str, db: Session = Depends(get_db)):
    question_query = db.query(Question).filter(Question.id == id).first()
    if not question_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Question has not found')
    return question_query


@router.patch('/{id}', response_model=question_schema.QuestionResponse)
def update_question(id:uuid.UUID, question: question_schema.UpdateQuestionSchema,
                    question_to_update = Depends(question_middleware.check_question_by_id),
                    db: Session = Depends(get_db)):
    question_to_update.update(question.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return question_to_update.first()


@router.delete('/{id}')
def delete_question(id:uuid.UUID, 
                    question_to_delete = Depends(question_middleware.check_question_by_id),
                    db: Session = Depends(get_db)):
    question_to_delete.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
