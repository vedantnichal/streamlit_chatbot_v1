import streamlit as st
from backend import workflow, return_threads
from langchain_core.messages import HumanMessage
import uuid

#generate threadid
def generate_thread():
    thread_id= uuid.uuid4()
    if thread_id not in st.session_state['thread_list']:
        st.session_state['thread_list'].append(thread_id)
        return thread_id
    else:
        generate_thread()

#get the messages
def get_chat_history(id):
    try:
        generic_chat= workflow.get_state(config= {'configurable': {'thread_id': id}}).values['messages']
        temp= []
        for items in generic_chat:
            if isinstance(items, HumanMessage):
                role= "user"
                content= items.content
                temp.append({'role': role, 'content': content})
            else:
                temp.append({'role': 'assistant', 'content': items.content})
        return temp
    except:
        return []

#reset chat
def reset_chat():
    st.session_state['thread_id']= generate_thread()
    st.session_state['chat_history']=[]

#resume chat
def resume_thread(id):
    st.session_state['thread_id']= id
    st.session_state['chat_history']= get_chat_history(id)

# session
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
if 'thread_list' not in st.session_state:
    st.session_state['thread_list']=return_threads()
if 'thread_id' not in st.session_state:
    st.session_state['thread_id']= generate_thread()

# sidebar
st.sidebar.title("Chatbot")
if st.sidebar.button("New Chat"):
    reset_chat()
st.sidebar.header("Current Conversation")
st.sidebar.text(st.session_state['thread_id'])
st.sidebar.header("Past Conversations")
for id in st.session_state['thread_list'][::-1]:
    if st.sidebar.button(id):
        resume_thread(id)


for items in st.session_state['chat_history']:
        with st.chat_message(items['role']):
            st.text(items['content'])

#user input
user_input= st.chat_input('Type here')

#response and printing + streaming
if user_input:
    st.session_state['chat_history'].append({'role': 'user', 'content': user_input})
    # response= workflow.invoke({'messages': [HumanMessage(content=user_input)]}, config= config)
    with st.chat_message('user'):
        st.text(user_input)

    with st.chat_message('assistant'):
        response= st.write_stream(
            message_chunk.content for message_chunk, metadata in workflow.stream(
                {'messages': [HumanMessage(content= user_input)]},
                config= {'configurable': {'thread_id': st.session_state['thread_id']}},
                stream_mode= 'messages'
            )
        )
    message= response
    st.session_state['chat_history'].append({'role': 'assistant', 'content': message})