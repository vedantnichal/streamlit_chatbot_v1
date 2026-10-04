from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
import streamlit as st

GROQ_API_KEY= st.secrets["GROQ_API_KEY"]

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

checkptr= InMemorySaver()
thread_id= 'user_1'
config= {"configurable": {"thread_id": thread_id}}

workflow=graph.compile(checkpointer= checkptr)
