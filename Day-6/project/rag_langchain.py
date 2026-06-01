from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

# loading 
def load_document(path):
    print("Loading document...")
    loader = TextLoader(path, encoding="utf-8")
    documents = loader.load()
    print(f"Loaded {len(documents)} document")
    return documents


# split into the chunks
def split_documents(documents):
    print("\n Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = splitter.split_documents(documents)
    print(f"Total chunks: {len(chunks)}")
    return chunks

# create vector store
def create_vectorstore(chunks):
    print("\nCreating embeddings...")
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="bootcamp_docs"
    )
    print(f"Vectorstore created with {len(chunks)} chunks")
    return vectorstore

# search
def search(question, vectorstore, top_k=3):
    print(f"\nQuestion: {question}")
    results = vectorstore.similarity_search(question, k=top_k)
    return results

# main
if __name__ == "__main__":
    # Load
    documents = load_document("docs/sample.txt")

    # Split
    chunks = split_documents(documents)

    # Store
    vectorstore = create_vectorstore(chunks)

    # Search
    questions = [
        "What is the refund policy?",
        "How many days attendance is required?",
        "When are certificates issued?"
    ]

    print("\n" + "="*50)
    print("SEARCH RESULTS")
    print("="*50)

    for question in questions:
        results = search(question, vectorstore)
        print("Relevant chunks:")
        for i, doc in enumerate(results):
            print(f"Chunk {i+1}: {doc.page_content[:100]}...")
        print()

    print("LangChain RAG Complete!")