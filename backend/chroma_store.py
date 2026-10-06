# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma

from langchain_huggingface import HuggingFaceEmbeddings
from backend.config import CHROMA_DB_DIR, COLLECTION_NAME, EMBEDDING_MODEL_NAME


def get_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)


def get_db():
    embeddings = get_embeddings()
    db = Chroma(
        persist_directory=CHROMA_DB_DIR,
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings
    )
    return db


def get_retriever(k=5):
    db = get_db()
    return db.as_retriever(search_kwargs={"k": k})

print("ChromaDB retriever is ready to use")