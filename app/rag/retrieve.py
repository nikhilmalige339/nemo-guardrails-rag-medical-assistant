from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

VECTOR_DB_PATH = os.path.join(BASE_DIR, "vector_db")

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory=VECTOR_DB_PATH,
    embedding_function=embedding
)

retriever = vectordb.as_retriever(
    search_kwargs={"k": 3}
)

def retrieve_context(query):

    docs = retriever.invoke(query)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    return context