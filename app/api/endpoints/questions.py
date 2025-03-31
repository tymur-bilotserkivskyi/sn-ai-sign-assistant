from fastapi import APIRouter
from app.models.schema import Question
from app.core.gpt_client import ask_main

router = APIRouter()

@router.post("/ask")
def ask(q: Question):
    answer = ask_main(question=q.question, context=q.context, main_id=q.id)
    return {"answer": answer}
