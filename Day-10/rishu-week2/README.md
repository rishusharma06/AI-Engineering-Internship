# 🤖 Chat With Documents Agent

This project is a simple AI-powered chatbot that can answer questions from documents using **RAG**, **LangGraph**, **ChromaDB**, and **Mistral AI**.

The system retrieves relevant document chunks and generates answers using an LLM.
It can also use tools like a current time function when needed.

---

# 🚀 Features

* Chat with custom documents
* RAG-based retrieval system
* LangGraph workflow
* ChromaDB vector storage
* Mistral AI integration
* Simple tool calling
* Source-based answers

---

# 🛠️ Tech Stack

* Python
* LangChain
* LangGraph
* ChromaDB
* Mistral AI
* dotenv

---

# 📁 Project Structure

```bash id="4wc7u1"
rishu-week2/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── ai.txt
│   ├── ml.txt
│   └── rag.txt
│
├── ingest/
│   └── ingest.py
│
├── agent/
│   ├── graph.py
│   └── tools.py
│
└── vectorstore/
```

---

# ⚙️ Setup

## 1. Install Dependencies

```bash id="obvp80"
pip install -r requirements.txt
```

---

## 2. Create `.env`

```env id="06txwt"
MISTRAL_API_KEY=your_api_key
```

---

## 3. Ingest Documents

```bash id="9q7q3y"
python ingest/ingest.py
```

This step:

* loads documents
* creates chunks
* generates embeddings
* stores vectors in ChromaDB

---

## 4. Run the Project

```bash id="48zcce"
python app.py
```

---

# 🔄 Workflow

```text id="r2b7wj"
User Question
      ↓
LangGraph Agent
      ↓
Retrieve Context (if needed)
      ↓
Generate Answer using Mistral AI
      ↓
Final Response
```

---


# 🧠 Concepts Used

* Embeddings
* Chunking
* Vector Search
* Retrieval Augmented Generation
* Conditional Routing
* Tool Calling

---

# 🛠️ Tool Added

### Current Time Tool

The agent can return the current system time if the user asks for it.

Example:

```text id="1cb0tx"
What is the current time?
```

---


