import streamlit as st
from bot import Bot


def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if 'bot' not in st.session_state:
        st.session_state.bot = Bot()


def display_chat_messages():
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

def handle_user_input():
    if prompt := st.chat_input('what is up?'):
        with st.chat_message('user'):
            st.markdown(prompt)

        st.session_state.messages.append({'role': 'user', 'content': prompt})

        bot_response = st.session_state.bot.chat(prompt)
        response = f'Ro Båt: {bot_response}'

        with st.chat_message('assistant'):
            st.markdown(response)

        st.session_state.messages.append({'role': 'assistant', 'content': response})

def layout():
    st.title('chatting with RO BÅT')
    st.write('Ro Båt is a funny robot that can help you out with programming tasks. However he does not directly answer your question, but usually he asks another question back.')

    display_chat_messages()
    handle_user_input()

    st.write(st.session_state)

if __name__ == "__main__":
    initialize_session_state()
    layout()