from qa_agent import GroqChatbot
import streamlit as st

st.title("AI DryLabs Q&A Chatbot")

if "chatbot" not in st.session_state:
    st.session_state.chatbot = GroqChatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question from the PDF..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = st.session_state.chatbot.get_response(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
