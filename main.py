from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from routers import question_router as QuestionRouter
from routers import answer_router

app = FastAPI(title = "Proviza API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(QuestionRouter.router, tags=['Questions'], prefix='/api/v1/questions')
app.include_router(answer_router.router, tags=['Answers'], prefix='/api/v1/answers')
