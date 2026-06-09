import streamlit as st

from chatbot.gemini_client import get_response
from chatbot.prompts import SYSTEM_PROMPT

st.set_page_config(page_title="Career Advisor Chatbot",page_icon="🤖",layout="wide")
st.title("🤖 Career Advisor Chatbot")
st.markdown("Ask me anything about careers, skills, certifications, and learning paths.")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "system_prompt_added" not in st.session_state:
    st.session_state.messages.append(
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    )
    st.session_state.system_prompt_added = True


for message in st.session_state.messages:
    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_prompt = st.chat_input("Ask your career question...")

if user_prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = get_response(st.session_state.messages,user_prompt)
            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )