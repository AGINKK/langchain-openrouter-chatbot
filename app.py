
import streamlit as st
from langchain_openrouter import ChatOpenRouter

st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 My AI Chatbot")
st.caption("Powered by Python, LangChain and OpenRouter")

with st.sidebar:
    st.header("About")
    st.write("A beginner AI chatbot built with LangChain.")
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_model = ChatOpenRouter(
    model="openrouter/free",
    temperature=0.7
)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat_model.invoke(
                    [
                        (
                            "system",
                            "You are a helpful chatbot. "
                            "Answer in simple English."
                        )
                    ]
                    + [
                        (
                            "human" if m["role"] == "user" else "ai",
                            m["content"]
                        )
                        for m in st.session_state.messages
                    ]
                )

                answer = response.content
                st.markdown(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as error:
        st.error(
            "Sorry, the AI could not respond. "
            "Check your API key, model availability, "
            "internet connection and OpenRouter usage limits."
        )
        st.caption(str(error))