from openai import OpenAI
import streamlit as st

with st.sidebar:
    password_app = st.text_input("Nhập Password", key="password_app", type="password")
    # openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    # "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    # "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    # "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"
if password_app == '91299':
    openai_api_key = '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'
    password = True
else:
    password = False
st.title("💬 Chat với cả bot cơ mà")
st.caption("🚀 Chatbot test of tetchies")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Tớ có thể giúp gì cho cậu ?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if password is False:
        st.info("Vui lòng nhập đúng pass nhá!")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)