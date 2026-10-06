# import os
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_unstructured.document_loaders import UnstructuredPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings
# from backend.config import CHROMA_DB_DIR,COLLECTION_NAME,EMBEDDING_MODEL_NAME

# PDF_FOLDER = "data/raw_docs" 

# def load_pdfs():
#     docs = []
#     for file in os.listdir(PDF_FOLDER):
#         if file.endswith(".pdf"):
#             path = os.path.join(PDF_FOLDER, file)
#             print(f"Loading: {path}")
#             loader = PyPDFLoader(path)
#             docs.extend(loader.load()) 
#     return docs

# def split_docs(documents):
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=150
#     )
#     return splitter.split_documents(documents)


# def store_docs(chunks):
#     embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

#     db = Chroma.from_documents(
#         documents=chunks,
#         embedding=embeddings,
#         persist_directory=CHROMA_DB_DIR,
#         collection_name=COLLECTION_NAME
#     )

#     db.persist()
#     print("✅ Documents stored successfully into ChromaDB")


# if __name__ == "__main__":
#     documents = load_pdfs()
#     chunks = split_docs(documents)
#     store_docs(chunks)
#     print(f"Total chunks stored: {len(chunks)}")

import os
# Use the correct community path + standard pypdf underneath
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from backend.config import CHROMA_DB_DIR, COLLECTION_NAME, EMBEDDING_MODEL_NAME

PDF_FOLDER = "data/raw_docs" 

def load_pdfs():
    docs = []
    if not os.path.exists(PDF_FOLDER):
        print(f"❌ Error: The directory '{PDF_FOLDER}' does not exist.")
        return docs

    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            path = os.path.join(PDF_FOLDER, file)
            print(f"Loading: {path}")
            loader = PyPDFLoader(path)
            docs.extend(loader.load()) 
    return docs

def split_docs(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    return splitter.split_documents(documents)

def store_docs(chunks):
    if not chunks:
        print("⚠️ No document chunks found to store.")
        return

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    # Automatically persists data dynamically upon creation
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR,
        collection_name=COLLECTION_NAME
    )
    print("✅ Documents stored successfully into ChromaDB")

if __name__ == "__main__":
    documents = load_pdfs()
    if documents:
        chunks = split_docs(documents)
        store_docs(chunks)
        print(f"Total chunks stored: {len(chunks)}")
    else:
        print("❌ Ingestion aborted: No documents were loaded.")
