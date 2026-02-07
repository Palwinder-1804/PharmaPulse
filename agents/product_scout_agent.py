from crewai import Agent
from llm import scout_llm as llm


product_scout_agent = Agent(
    role="Pharmaceutical Product Competitive Intelligence Engine",

    goal=(
        "Identify products similar to the target pharmaceutical product "
        "and extract structured competitor intelligence in STRICT JSON format."
    ),

    backstory=(
        "You analyze pharmaceutical markets to identify competing products, "
        "their manufacturers, therapy focus, approval status, market share, "
        "and pricing position. You output only structured JSON."
    ),

    llm=llm,
    verbose=False,
    allow_delegation=False
)
