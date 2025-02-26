
from main import *
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
import langchain




# Model setup
model = init_chat_model("llama3-8b-8192", model_provider="groq")
search = TavilySearchResults(max_results=2)
tools = [search]
model_with_tools = model.bind_tools(tools)

# Debugging: Print model setup
print(model_with_tools)

# Invoke the agent with LangSmith tracing
  # Creates a named trace session
agent_executor = create_react_agent(model, tools)
response = agent_executor.invoke({"messages": [HumanMessage(content="what is the weather in Karachi")]})

# Debugging: Print response
print(response['messages'])
langchain.debug= True