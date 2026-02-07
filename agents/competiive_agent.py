from crewai import Agent
from llm import strategic_llm as llm


competitive_agent = Agent(
    role="Pharmaceutical Competitive Intelligence Engine",

    goal=(
        "Analyze pharmaceutical events and extract competitor "
        "positioning, product USP, and market strategy in STRICT JSON format."
    ),

    backstory=(
        "You specialize in identifying competitive differentiation, "
        "pricing strategy, innovation focus, and positioning advantages."
    ),

    llm=llm,
    verbose=False
)
