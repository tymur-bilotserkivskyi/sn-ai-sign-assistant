from fastapi import APIRouter, Body
import uuid
from app.core.vector_store import add_document
from app.api.endpoints.utils import chunk_text

router = APIRouter()

@router.post("/addtxt")
def add(text: str = Body(..., media_type="text/plain")):
    chunks = chunk_text(text)
    added_ids = []

    for i, chunk in enumerate(chunks):
        doc_id = f"{uuid.uuid4()}_chunk{i}"
        add_document(doc_id, chunk)
        added_ids.append(doc_id)

    return {"status": "document added", "chunks_added": len(added_ids)}
