from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage


# Load environment variables from the .env file
load_dotenv(dotenv_path="env\\.env")

# Access the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Access Langsmith environment variables
langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
langsmith_endpoint = os.getenv("LANGSMITH_ENDPOINT")
langsmith_project = os.getenv("LANGSMITH_PROJECT")
langsmith_tracing = os.getenv("LANGSMITH_TRACING")

#Acess the Tavily API key
Tavily_api_key = os.getenv("Tavily_API_KEY")

