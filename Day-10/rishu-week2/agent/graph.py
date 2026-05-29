from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv
from agent.tools import current_time_tool

load_dotenv()

# LLM
llm = ChatMistralAI(
    model="mistral-large-latest"
)

# Embeddings
embedding = MistralAIEmbeddings(
    model="mistral-embed"
)

# Load vector DB
vectorstore = Chroma(
    persist_directory="vectorstore",
    embedding_function=embedding
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# State
class AgentState(TypedDict):
    question: str
    context: List[str]
    answer: str

# Agent Node
def agent_node(state):
    question = state["question"]

    if "time" in question.lower():
        answer = current_time_tool()

        return {
            "question": question,
            "context": [],
            "answer": answer
        }

    return state

# Retrieve Node
def retrieve_node(state):
    question = state["question"]

    docs = retriever.invoke(question)

    context = []

    for i, doc in enumerate(docs):
        source = doc.metadata.get("source", "unknown")
        text = doc.page_content

        context.append(
            f"[Chunk {i}] Source: {source}\n{text}"
        )

    return {
        "question": question,
        "context": context,
        "answer": ""
    }

# Generate Node
def generate_node(state):
    question = state["question"]
    context = "\n".join(state["context"])

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Also mention the chunk sources used.
"""

    response = llm.invoke(prompt)

    return {
        "question": question,
        "context": state["context"],
        "answer": response.content
    }

# Decide retrieval
def should_retrieve(state):
    question = state["question"]

    if "time" in question.lower():
        return "end"

    return "retrieve"

# Graph
builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
builder.add_node("retrieve", retrieve_node)
builder.add_node("generate", generate_node)

builder.add_edge(START, "agent")

builder.add_conditional_edges(
    "agent",
    should_retrieve,
    {
        "retrieve": "retrieve",
        "end": END
    }
)

builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

graph = builder.compile()