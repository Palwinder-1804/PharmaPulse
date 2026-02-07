from crewai import Agent
from llm import strategic_llm as llm


strategy_agent = Agent(
    role="Pharmaceutical Go-To-Market and Defense Strategy Engine",

    goal=(
        "Generate structured product launch strategy for new products and "
        "market defense strategy for existing products in STRICT JSON format."
    ),

    backstory=(
        "You provide executive-level pharmaceutical strategy recommendations "
        "focused on launch planning, positioning, competitive response, "
        "and long-term market sustainability."
    ),

    llm=llm,
    verbose=False
)
