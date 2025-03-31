import chromadb
from chromadb.config import Settings
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import os
from dotenv import load_dotenv

load_dotenv()

embedding_func = OpenAIEmbeddingFunction(api_key=os.getenv("OPENAI_API_KEY"), model_name="text-embedding-3-small")

chroma_client = chromadb.PersistentClient(path="./chroma_data")
def get_collection(id: str):
    """
    Get a collection by ID.
    """
    return chroma_client.get_or_create_collection(name=id, embedding_function=embedding_func)
# collection = chroma_client.get_or_create_collection(name="documents", embedding_function=embedding_func)

def add_document(doc_id: str, text: str, collection_name: str = "documents"):
    collection = get_collection(id=collection_name)
    collection.add(documents=[text], ids=[doc_id])

def query_similar_documents(query: str, n_results: int = 3, collection_name: str = "documents"):
    collection = get_collection(id=collection_name)
    return collection.query(query_texts=[query], n_results=n_results)

def get_document(id: str, collection_name: str = "documents"):
    """
    Get a document by ID.
    """
    collection = get_collection(id=collection_name)
    return collection.get(ids=[id])
