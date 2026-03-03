from google.adk.agents.llm_agent import Agent
from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")

def search(query:str) -> dict[str,any]:
    """
        This tool searches the internet for the user's queries.
    """
    tavily_client = TavilyClient(api_key=TAVILY_API_KEY)
    response = tavily_client.search(query)

    print(response)
    return response
    

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[search]
)



