import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CHROMA_DB_DIR = "vectordb/chroma_db"
COLLECTION_NAME = "banking_insurance_docs"

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

TOP_K = 5