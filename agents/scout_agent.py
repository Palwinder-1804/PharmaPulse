from crewai import Agent
from tools.search_tool import market_search_tool as search_tool
from llm import scout_llm as llm


scout_agent = Agent(
    role="Pharmaceutical Market Data Extraction Engine",

    goal=(
        "Identify high-impact pharmaceutical industry events "
        "from real-time search data and return structured JSON. "
        "Focus strictly on strategic events affecting competition, "
        "pricing, regulation, product launches, mergers, and expansion."
    ),

    backstory=(
        "You are a structured data extraction engine used in a real-time "
        "pharmaceutical intelligence system. "
        "You do not generate reports. "
        "You extract structured, machine-readable strategic events."
    ),

    tools=[search_tool],

    llm=llm,

    verbose=False,  # Turn off for production

    allow_delegation=False
)
