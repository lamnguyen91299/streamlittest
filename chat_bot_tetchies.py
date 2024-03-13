from openai import OpenAI
import streamlit as st

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

with st.sidebar:
    password_app = st.text_input("Nhập Password", key="password_app", type="password")
    # openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    # "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    # "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    # "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"
    on = st.toggle('Chế độ vô tri')

if on:
    no_brain_mode_text = 'Hãy tạo ra một câu đùa vô tri với nội dung '
else:
    no_brain_mode_text = ''

if password_app == '91299':
    openai_api_key = decrypt('xp-jXagRaRDIPvg4Z41dkbEY3GqgpKOrg3R4x8YCer8kQ0wQJvs',5)
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
    st.session_state.messages.append({"role": "user", "content": no_brain_mode_text + prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)