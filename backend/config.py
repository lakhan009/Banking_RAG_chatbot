import os
from dotenv import load_dotenv

load_dotenv()
# OPENAI_API_KEY = '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'
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
 

CHROMA_DB_DIR = "vectordb/chroma_db"
COLLECTION_NAME = "banking_insurance_docs"

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

TOP_K = 5
