from summarize_agent import summarize_url
import asyncio
import streamlit as st

st.title("Webpage Summarizer")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Enter URL to summarize"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Summarizing..."):
            try:
                response = asyncio.run(summarize_url(prompt))
            except Exception as e:
                response = f"Error: {str(e)}"
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})