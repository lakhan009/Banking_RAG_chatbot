from langchain_openai import ChatOpenAI
# from langchain.chains import RetrievalQA
from langchain_classic.chains import RetrievalQA

# from langchain.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate

from backend.chroma_store import get_retriever
from backend.prompt_templates import BANKING_PROMPT
from backend.config import TOP_K


def build_rag_chain():
    retriever = get_retriever(k=TOP_K)

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2
    )

    prompt = PromptTemplate(
        template=BANKING_PROMPT,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

    return qa_chain


def ask(query: str):
    chain = build_rag_chain()
    result = chain.invoke({"query": query})

    answer = result["result"]
    sources = result["source_documents"]

    return answer, sources