%%writefile app.py
import os
from openai import OpenAI
import streamlit as st
from google.colab import userdata

OPENAI_API_KEY = userdata.get("chatbot") # Ensure this secret is set in Colab's Secrets
client = OpenAI(api_key=OPENAI_API_KEY)

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")
st.write("Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=st.session_state.messages
        )

        reply = response.choices[0].message.content

        st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
