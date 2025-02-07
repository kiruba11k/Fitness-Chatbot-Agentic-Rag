import os
import uuid
import streamlit as st
from main import app

# Streamlit UI Configuration
st.set_page_config(page_title="🏋️ Fitness Chatbot", page_icon="🏋️", layout="wide")
st.markdown("""
    <style>
    .chat-container {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .user-message {
        background-color: #d1e7dd;
        border-left: 5px solid #0f5132;
        padding: 10px;
        border-radius: 8px;
        margin: 5px 0;
    }
    .assistant-message {
        background-color: #f8d7da;
        border-left: 5px solid #842029;
        padding: 10px;
        border-radius: 8px;
        margin: 5px 0;
    }
    .clear-button {
        background-color: #dc3545;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 5px;
        cursor: pointer;
    }
    .clear-button:hover {
        background-color: #c82333;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏋️ Your Personal Fitness Assistant")
st.subheader("Ask me anything about fitness, diet, or nutrition!")

# Initialize chat history if not present
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Generate unique IDs for session management
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = f"thread_{uuid.uuid4().hex}"
if 'session_id' not in st.session_state:  # Changed from checkpoint_id to session_id
    st.session_state['session_id'] = f"session_{uuid.uuid4().hex}"

# Display chat history
for message in st.session_state['messages']:
    role_class = "user-message" if message['role'] == "user" else "assistant-message"
    st.markdown(f'<div class="chat-container {role_class}">{message["content"]}</div>', unsafe_allow_html=True)

# User input
user_input = st.text_input("Type your question here...")

if st.button("Send") and user_input:
    # Display user message
    st.session_state['messages'].append({"role": "user", "content": user_input})
    st.markdown(f'<div class="chat-container user-message">{user_input}</div>', unsafe_allow_html=True)

    # Invoke AI assistant with thread_id and session_id (renamed)
    response = app.invoke({
        "messages": st.session_state['messages'],
        "thread_id": st.session_state['thread_id'],          # Required by Checkpointer
        "session_id": st.session_state['session_id']         # Changed from checkpoint_id to session_id
    })

    ai_reply = response['messages'][0].content

    # Display AI response
    st.session_state['messages'].append({"role": "assistant", "content": ai_reply})
    st.markdown(f'<div class="chat-container assistant-message">{ai_reply}</div>', unsafe_allow_html=True)

# Option to clear chat
if st.button("Clear Chat", key="clear", help="Click to reset the conversation"):
    st.session_state['messages'] = []
    st.experimental_rerun()
