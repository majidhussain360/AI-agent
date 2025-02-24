from main import *
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

#Tavily search engine invoke check 
'''search = TavilySearchResults(max_results=2)
search_results = search.invoke("what is the weather in SF")
print(search_results)
tools = [search]'''
# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.

#Initial message invoke test
model = init_chat_model("llama3-8b-8192", model_provider="groq")
response = model.invoke([HumanMessage(content="hi!")])
print(response.content)