from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# Load documents
files = [
    "data/ai.txt",
    "data/ml.txt",
    "data/rag.txt"
]

documents = []

for file in files:
    loader = TextLoader(file)
    documents.extend(loader.load())

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

# Embedding model
embedding = MistralAIEmbeddings(
    model="mistral-embed"
)

# Store in Chroma
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding,
    persist_directory="vectorstore"
)

vectorstore.persist()

print("Documents embedded successfully")