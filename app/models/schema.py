from pydantic import BaseModel

class Document(BaseModel):
    id: str
    text: str

class Question(BaseModel):
    question: str
    context: str = None
    id: str = "main"

class Query(BaseModel):
    query: str
    n_results: int = 3
    id: str = "documents"

class Suggest(BaseModel):
    id: str = "documents"
