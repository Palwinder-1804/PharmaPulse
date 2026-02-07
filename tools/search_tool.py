import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

load_dotenv()

# 🔹 Market News Search Tool
market_search_tool = SerperDevTool(
    n_results=6
)

# 🔹 Product Intelligence Search Tool
product_search_tool = SerperDevTool(
    n_results=8
)
