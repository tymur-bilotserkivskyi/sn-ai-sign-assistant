from fastapi import APIRouter
from app.models.schema import Question
from app.core.gpt_client import ask_suggest
from app.models.schema import Suggest

router = APIRouter()

@router.get("/suggestion")
def ask(q: Suggest):
    answer = ask_suggest()
    return {"answer": answer}
