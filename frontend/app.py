import os
import requests
import streamlit as st

API_URL = os.getenv("NEWS_AGENT_API_URL", "http://127.0.0.1:8089/ask")

st.set_page_config(page_title="News Research Assistant", page_icon="📰")
st.title("📰 News Research Assistant")
st.caption("Ask a question about current news. Answers depend on available search results.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask about the latest news...")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching for news..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=120,
                )
                response.raise_for_status()
                answer = response.json().get("answer", "No answer returned.")
            except requests.RequestException as exc:
                answer = (
                    "Could not reach the backend API. Make sure FastAPI is running "
                    f"at {API_URL}. Details: {exc}"
                )
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
