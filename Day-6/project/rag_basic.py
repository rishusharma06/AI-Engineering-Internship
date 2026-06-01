from sentence_transformers import SentenceTransformer
import chromadb
import os

def load_document(path):
    with open(path, "r", encoding = "utf-8") as f:
        return f.read()


def chunk_text(text, chunk_size=30, overlap=5):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        # Take chunk_size words
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)

        # Move forward by (chunk_size - overlap)
        start += chunk_size - overlap

    return chunks

def setup_vectorstore(chunks):
    # Initialize embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Initialize Chroma client
    client = chromadb.Client()
    collection = client.create_collection("bootcamp_docs")

    # Embed and store chunks
    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk).tolist()
        collection.add(
            ids=[f"chunk_{i}"],
            embeddings=[embedding],
            documents=[chunk]
        )
        print(f"Stored chunk {i+1}/{len(chunks)}")

    return collection, model

def search(question, collection, model, top_k=3):
    # Embed the question
    question_embedding = model.encode(question).tolist()

    # Search for similar chunks
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k
    )

    return results["documents"][0] 


if __name__ == "__main__":
    print(" Loading document...")
    text = load_document("docs/sample.txt")

    print(" Chunking text...")
    chunks = chunk_text(text, chunk_size=50, overlap=10)
    print(f"Total chunks: {len(chunks)}")

    print(" Creating embeddings and storing...")
    collection, model = setup_vectorstore(chunks)

    questions = [
        "What is the refund policy?",
        "How many days attendance is required?",
        "When are certificates issued?"
    ]

    print("SEARCH RESULTS")
    print("="*50)

    for question in questions:
        print(f"\n Question: {question}")
        chunks_found = search(question, collection, model)
        print(" Relevant chunks found:")
        for i, chunk in enumerate(chunks_found):
            print(f"  Chunk {i+1}: {chunk[:100]}...")