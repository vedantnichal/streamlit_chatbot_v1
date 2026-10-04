import streamlit as st
from backend import workflow, config
from langchain_core.messages import HumanMessage

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
# chat_history=[]

user_input= st.chat_input('Type here')

if user_input:
    st.session_state['chat_history'].append({'role': 'user', 'content': user_input})
    # response= workflow.invoke({'messages': [HumanMessage(content=user_input)]}, config= config)
    for items in st.session_state['chat_history']:
        with st.chat_message(items['role']):
            st.text(items['content'])

    with st.chat_message('assistant'):
        response= st.write_stream(
            message_chunk.content for message_chunk, metadata in workflow.stream(
                {'messages': [HumanMessage(content= user_input)]},
                config= config,
                stream_mode= 'messages'
            )
        )
    message= response
    st.session_state['chat_history'].append({'role': 'assistant', 'content': message})