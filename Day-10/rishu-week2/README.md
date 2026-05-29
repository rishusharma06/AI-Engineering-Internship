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

# 💬 Example Questions

```text id="r7pwxv"
What is RAG?
```

```text id="gy8t6w"
Explain Machine Learning.
```

```text id="ckx0o0"
What is the current time?
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

# 📌 Why This Project?

This project demonstrates:

* RAG pipeline implementation
* Vector database usage
* LangGraph agent flow
* Tool calling
* LLM integration with Mistral AI

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

# 📷 Sample Output

```text id="6gzk0x"
Ask Question: What is RAG?

Answer:

RAG stands for Retrieval Augmented Generation.
It combines retrieval systems with language models for better answers.

Source:
data/rag.txt
```

---

# 👨‍💻 Author

Rishu Sharma
AI Engineering Bootcamp — Week 2 Assessment
