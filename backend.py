from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
import streamlit as st
import sqlite3

GROQ_API_KEY= st.secrets["GROQ_API_KEY"]
conn=sqlite3.connect(database='chatbot.db', check_same_thread=False)

llm=ChatGroq(model='openai/gpt-oss-120b')

class chatstate(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat(state: chatstate):
    messages= state['messages']
    response= llm.invoke(messages)
    return {"messages": response}

graph= StateGraph(chatstate)
graph.add_node('chat', chat)
graph.add_edge(START, 'chat')
graph.add_edge('chat', END)

checkptr= SqliteSaver(conn=conn)

workflow=graph.compile(checkpointer= checkptr)

def return_threads():
    threads=set()
    for checkptrs in checkptr.list(None):
        threads.add(checkptrs.config['configurable']['thread_id'])
    return(list(threads))

return_threads()
# thread_id= 'user_1'
# config= {"configurable": {"thread_id": thread_id}}
# response=workflow.invoke(
#     {'messages': [HumanMessage(content="what is my name")]},
#     config= config
# )
# print(response)