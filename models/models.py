import uuid
from database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Question(Base):
    __tablename__ = "questions"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    question = Column(String,  nullable=False)
    category = Column(String,  nullable=False)
    is_active = Column(Boolean, nullable=False, server_default='True')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=True, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=True, server_default=text("now()"))

class Answer(Base):
    __tablename__ = "answers"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    question_id = Column(UUID(as_uuid=True), ForeignKey(
        'questions.id', ondelete='CASCADE'), nullable=False)
    answer = Column(String,  nullable=False)
    image = Column(String,  nullable=True)
    is_correct = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False, server_default='True')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=True, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=True, server_default=text("now()"))
    question = relationship('Question')
