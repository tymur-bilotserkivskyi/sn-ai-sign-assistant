from fastapi import APIRouter, UploadFile, File, HTTPException
import fitz  # PyMuPDF
import uuid
from app.core.vector_store import add_document, query_similar_documents
from app.models.schema import Query
from app.api.endpoints.utils import chunk_text

router = APIRouter()

@router.post("/addpdf")
async def add_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    contents = await file.read()
    try:
        doc = fitz.open(stream=contents, filetype="pdf")
        full_text = ""
        for page in doc:
            full_text += page.get_text()

        title = file.filename.replace(".pdf", "").strip()
        text_with_title = f"Title: {title}\n\n{full_text}"
        chunks = chunk_text(text_with_title)

        added_ids = []
        for i, chunk in enumerate(chunks):
            doc_id = f"{uuid.uuid4()}_chunk{i}"
            add_document(doc_id, chunk)
            added_ids.append(doc_id)

        return {
            "status": "PDF processed and added",
            "chunks_added": len(added_ids),
            "document_title": title
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")
    
@router.post("/main/addpdf")
async def add_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    contents = await file.read()
    try:
        doc = fitz.open(stream=contents, filetype="pdf")
        full_text = ""
        for page in doc:
            full_text += page.get_text()

        title = file.filename.replace(".pdf", "").strip()
        text_with_title = f"Title: {title}\n\n{full_text}"
        
        add_document(doc_id="main", text=text_with_title, collection_name="main")

        return {
            "status": "PDF processed and added",
            "document_title": title
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")


@router.get("/getsimilar")
# async def get_similar_documents(question: str, n_results: int = 3, id: str = "documents"):
async def get_similar_documents(data: Query):
    if not data:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    try:
        results = query_similar_documents(data.query, data.n_results)
        return {
            "status": "success",
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error querying similar documents: {str(e)}")
