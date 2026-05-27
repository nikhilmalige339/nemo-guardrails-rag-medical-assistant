# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings
# import os

# PDF_FOLDER = "../../docs"

# documents = []

# for file in os.listdir(PDF_FOLDER):

#     if file.endswith(".pdf"):

#         loader = PyPDFLoader(
#             os.path.join(PDF_FOLDER, file)
#         )

#         documents.extend(loader.load())

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=50
# )

# chunks = splitter.split_documents(documents)

# embedding = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# vectordb = Chroma.from_documents(
#     documents=chunks,
#     embedding=embedding,
#     persist_directory="vector_db"
# )

# vectordb.persist()

# print("Documents embedded successfully!")

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

################################################
# ONLY PUBLIC DOCUMENTS
################################################

PDF_FOLDER = "../../docs/public"

documents = []

################################################
# LOAD ONLY PUBLIC PDFs
################################################

for file in os.listdir(PDF_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(PDF_FOLDER, file)

        print(f"Loading: {file}")

        loader = PyPDFLoader(pdf_path)

        documents.extend(loader.load())

################################################
# SPLIT DOCUMENTS
################################################

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

################################################
# EMBEDDING MODEL
################################################

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

################################################
# CREATE VECTOR DATABASE
################################################

vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="vector_db"
)

vectordb.persist()

print("Public hospital documents embedded successfully!")