from openai import OpenAI
import os
from dotenv import load_dotenv
from app.core.vector_store import query_similar_documents, get_document, get_collection
from app.templates.prompt import PROMPT_TEMPLATE, SUGGEST_TEMPLATE

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def ask_gpt(input: str) -> str:
    response = client.responses.create(
        model="gpt-3.5-turbo",
        # model="gpt-4o",
        input=input,
    )
    return response

def ask_main(question: str, context: str = None, main_id: str = "main", doc_collection_id: str = "documents") -> str:
    results = query_similar_documents(question)
    additional_data = "\n---\n".join(results[doc_collection_id][0]) if results[doc_collection_id] else ""
    document_text = get_document(id=main_id, collection_name=main_id)

    prompt = PROMPT_TEMPLATE.format(
        document_text=document_text,
        additional_data=additional_data,
        question=question,
        context=context,
    )

    return ask_gpt(prompt)

def ask_suggest(main_id: str = "main", doc_collection_id: str = "documents") -> str:
    documents = "\n---\n".join(get_collection(id=doc_collection_id).get())
    main = get_document(id=main_id, collection_name=main_id)
    prompt = SUGGEST_TEMPLATE.format(
        document_text=main,
        additional_data=documents,
    )

    return ask_gpt(prompt)