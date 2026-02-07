from crewai import Agent
from llm import strategic_llm as llm


supervisor_agent = Agent(
    role="Pharmaceutical Executive Decision Engine",

    goal=(
        "Review strategic intelligence and produce final executive-level "
        "decision summary in STRICT JSON format."
    ),

    backstory=(
        "You operate at CEO-level. You produce structured executive "
        "decision intelligence optimized for dashboards and APIs."
    ),

    llm=llm,
    verbose=False
)
