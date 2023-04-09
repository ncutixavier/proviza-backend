import uuid
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import get_db
from schemas import answer_schema
from models.models import Answer
from middlewares import question_middleware, answer_middleware

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=answer_schema.AnswerResponse)
def create_answer(answer: answer_schema.CreateAnswerSchema = Depends(question_middleware.check_question_id_from_answer), 
                  db: Session = Depends(get_db)):
    new_answer = Answer(**answer.dict())
    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)
    return new_answer


@router.get('/{question_id}/question', response_model=answer_schema.ListAnswerResponse)
def get_answer_for_specific_question(question_id = Depends(question_middleware.check_question_id_exist), 
                                     db: Session = Depends(get_db)):
    answers = db.query(Answer).filter(Answer.question_id == question_id).all()
    return {'results': len(answers), 'answers': answers}


@router.patch('/{id}', response_model=answer_schema.AnswerResponse)
def update_answer(id:uuid.UUID, answer: answer_schema.UpdateAnswerSchema,
                    answer_to_update = Depends(answer_middleware.check_answer_by_id),
                    db: Session = Depends(get_db)):
    answer_to_update.update(answer.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return answer_to_update.first()

@router.delete('/{id}')
def delete_question(id:uuid.UUID, 
                    answer_to_delete = Depends(answer_middleware.check_answer_by_id),
                    db: Session = Depends(get_db)):
    answer_to_delete.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
