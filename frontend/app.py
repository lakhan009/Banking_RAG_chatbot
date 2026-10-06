import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="Banking RAG Chatbot", layout="centered")

st.title("Banking & Insurance RAG Chatbot")
st.write("Ask questions related to banking or insurance policies.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 1. Wrapped in a form to allow native input clearing on submit
with st.form("chat_form", clear_on_submit=True):
    question = st.text_input("Ask your question:")
    submit_button = st.form_submit_button("Send")

if submit_button and question.strip() != "":
    try:
        response = requests.post(API_URL, json={"question": question})
        # Check if the backend API returned a success status code
        if response.status_code == 200:
            result = response.json()
            st.session_state.chat_history.append(("You", question))
            st.session_state.chat_history.append(("Bot", result.get("answer", "No response content.")))
        else:
            st.error(f"Backend error: Received status code {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("Unable to connect to the backend server. Make sure your FastAPI/Uvicorn app is running at port 8000!")

# Display chat history
for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"** You:** {msg}")
    else:
        st.markdown(f"** Bot:** {msg}")
