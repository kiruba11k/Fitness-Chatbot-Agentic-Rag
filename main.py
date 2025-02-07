from langchain_core.prompts import PromptTemplate
from langchain_core.tools import create_retriever_tool
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from typing import Sequence
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langgraph.graph.message import add_messages
from typing_extensions import Annotated, TypedDict
from langgraph.prebuilt import ToolNode
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["USER_AGENT"] = "AgenticLLM/1.0"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Load Data
doc_splits = WebBaseLoader("https://www.healthline.com/nutrition").load()
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
llm = ChatGroq(model_name="Gemma2-9b-It", api_key=GROQ_API_KEY)

# Vector Store
vectorstore = Chroma.from_documents(
    documents=doc_splits,
    collection_name="rag-chrome",
    embedding=embeddings
)
retriever = vectorstore.as_retriever()

# Retriever Tool
retriever_tool = create_retriever_tool(
    retriever,
    "retrieve_blog_posts",
    "Search and return information about fitness, diet, nutrition, and healthy food."
)
tools = [retriever_tool]

# Agent State
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    thread_id: str
    session_id: str  # Changed from custom_checkpoint_id to session_id

# Memory
memory = MemorySaver()

# AI Assistant Function
def ai_assistant(state: AgentState):
    messages = state['messages']
    thread_id = state['thread_id']

    if len(messages) > 1:
        question = messages[-1]['content']
        prompt = PromptTemplate(
            template="You are a helpful assistant. Answer the question: {question}",
            input_variables=["question"]
        )
        formatted_prompt = prompt.format(question=question)
        response = llm.invoke(formatted_prompt)
    else:
        llm_with_tool = llm.bind_tools(tools)
        response = llm_with_tool.invoke(messages)

    return {"messages": [response], "thread_id": thread_id, "session_id": state['session_id']}

# Workflow
workflow = StateGraph(AgentState)
workflow.add_node("My_Ai_Assistant", ai_assistant)
workflow.add_node("Vector_Retriever", ToolNode([retriever_tool]))
workflow.add_edge(START, "My_Ai_Assistant")
workflow.add_edge("My_Ai_Assistant", "Vector_Retriever")
workflow.add_edge("Vector_Retriever", END)

# Compile with Memory
app = workflow.compile(checkpointer=memory)

# Expose app for import
__all__ = ["app"]