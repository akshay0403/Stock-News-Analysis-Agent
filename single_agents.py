from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

# News Agent

news_agent = Agent(
    name = "News Agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = [
        'Search the latest financial news about Apple Stocks',
        'Summarize the top 5 news articles',
        'Provide key insights in markdown format for read'
    ],
    show_tool_calls = True,
    markdown = True,
    debug_mode = True
)
news_agent.print_response(
    "Summarize the latest financial news about Apple stock in markdown format.",
    stream = True
)