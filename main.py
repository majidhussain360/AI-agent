from dotenv import load_dotenv
import os



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

# ✅ Set LangSmith tracing via environment variable
os.environ["LANGCHAIN_TRACING_V2"] = "true"  # Enables tracing
os.environ["LANGCHAIN_PROJECT"] = "WeatherBot"  # Optional: Name your project
