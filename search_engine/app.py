from search_engine import SemanticSearchEngine
import streamlit as st

st.title("Search Agent")

if "search_engine" not in st.session_state:
    engine = SemanticSearchEngine()
    engine.add_documents([
        "Python is a versatile programming language used for web development, data science, and automation.",
        "Machine learning algorithms can automatically learn patterns from data without explicit programming.",
        "Deep learning is a subset of machine learning that uses neural networks with multiple layers.",
        "Natural language processing helps computers understand and generate human language.",
        "Data visualization is crucial for understanding complex datasets and communicating insights.",
        "Cloud computing provides on-demand access to computing resources over the internet.",
        "Cybersecurity protects digital systems from threats and unauthorized access.",
        "Blockchain technology creates immutable records through distributed consensus."
    ])
    st.session_state.search_engine = engine


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    results = st.session_state.search_engine.search(prompt, top_k=2)
    response = "\n".join(
        f"{i+1}. (Score: {r['similarity']:.3f}) {r['document']}" for i, r in enumerate(results)
    ) if results else "No relevant documents found."

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})