from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag_pipeline import ask

app = FastAPI(title="Banking Insurance RAG Chatbot")


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Banking/Insurance RAG Chatbot API is running"}


@app.post("/chat")
def chat(req: QueryRequest):
    answer, sources = ask(req.question)

    source_list = []
    for doc in sources:
        source_list.append({
            "source": doc.metadata.get("source", "unknown"),
            "content_preview": doc.page_content[:200]
        })

    return {
        "question": req.question,
        "answer": answer,
        "sources": source_list
    }