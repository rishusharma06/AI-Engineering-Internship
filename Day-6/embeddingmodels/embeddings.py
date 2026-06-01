import os
from dotenv import load_dotenv
#import API module
from langchain_huggingface import HuggingFaceEndpointEmbeddings

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    model="sentence-transformers/all-MiniLM-L6-v2",
)

text = "What is AI Engineering?"
# embed_query for one sentence and embed_document for multiple
single_embedding = embeddings.embed_query(text)

print(f"API Generated Vector Length: {len(single_embedding)}")
