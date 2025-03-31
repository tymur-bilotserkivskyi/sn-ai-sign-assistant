from fastapi import FastAPI
from app.api.endpoints import addtxt, questions, pdf, suggestion, health

app = FastAPI()

app.include_router(addtxt.router, prefix="/documents", tags=["Documents"])
app.include_router(pdf.router, prefix="/documents", tags=["PDF"])
app.include_router(questions.router, tags=["Questions"])
app.include_router(suggestion.router, tags=["Suggestion"])

app.include_router(health.router, tags=["Health"])