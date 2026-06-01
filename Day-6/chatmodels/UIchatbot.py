# app.py

from dotenv import load_dotenv
import os
import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# =========================
# Load Environment Variables
# =========================
load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# =========================
# Streamlit Page Config
# =========================
st.set_page_config(
    page_title="Funny AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# =========================
# Custom CSS
# =========================
st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

h1 {
    text-align: center;
    color: #38bdf8;
}

[data-testid="stChatMessage"] {
    border-radius: 15px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# Title
# =========================
st.title("🤖 Funny AI Chatbot")

# =========================
# Check API Key
# =========================
if not MISTRAL_API_KEY:
    st.error("❌ MISTRAL_API_KEY not found in .env file")
    st.stop()

# =========================
# Initialize Model
# =========================
try:
    model = ChatMistralAI(
        model="mistral-small-latest",
        temperature=0.9,
        api_key=MISTRAL_API_KEY
    )
except Exception as e:
    st.error(f"Model Initialization Error: {e}")
    st.stop()

# =========================
# Session State
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a funny AI chatbot.")
    ]

# =========================
# Display Chat Messages
# =========================
for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# =========================
# Chat Input
# =========================
prompt = st.chat_input("Type your message here...")

if prompt:

    # Store User Message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Display User Message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    try:
        response = model.invoke(st.session_state.messages)

        ai_response = response.content

    except Exception as e:
        ai_response = f"❌ Error: {str(e)}"

    # Store AI Response
    st.session_state.messages.append(
        AIMessage(content=ai_response)
    )

    # Display AI Response
    with st.chat_message("assistant"):
        st.markdown(ai_response)

# =========================
# Sidebar
# =========================
with st.sidebar:

    st.header("⚙️ Settings")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = [
            SystemMessage(content="You are a funny AI chatbot.")
        ]

        st.rerun()

    st.success("✅ Powered by Mistral + LangChain + Streamlit")