# LangGraph Streamlit Chatbot

A simple AI chatbot built with **Streamlit, LangGraph, and Groq**.

This project is also my learning project for **LangGraph**. I will continuously extend this application as I learn new LangGraph concepts such as memory, tools, agents, human-in-the-loop, persistence, and more.

---

## 🚀 Deployment

The application is deployed using **Streamlit Community Cloud**.


---

## 📌 Current Features

- 💬 Chat interface built with Streamlit
- 🤖 LLM-powered responses using Groq
- ⚡ Streaming responses in real time
- 🧠 LangGraph-based conversation workflow
- 💾 Conversation state using LangGraph's `InMemorySaver`
- 🧵 Thread-based configuration
- 🔐 API key management using Streamlit Secrets
- 📚 Designed to be extended as I learn more LangGraph concepts

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Streamlit | Web interface |
| LangGraph | Building the chatbot workflow |
| LangChain Core | Message handling |
| LangChain Groq | Groq LLM integration |
| Groq | LLM provider |
| python-dotenv | Environment variable management |

---

## 📂 Project Structure

```text
streamlit_chatbot_v1/
│
├── frontend.py          # Streamlit user interface
├── backend.py           # LangGraph chatbot workflow
├── requirements.txt     # Python dependencies
├── .gitignore           # Ignored files and secrets
└── README.md            # Project documentation
```
