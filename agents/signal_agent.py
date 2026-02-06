from crewai import Agent
from llm import strategic_llm as llm

signal_agent = Agent(
    role="Strategic Signal Analyst",

    goal=(
        "Analyze pharma news and classify events into strategic signals such as "
        "Competitive Threat, Market Opportunity, Pricing Shift, Regulatory Risk, "
        "or Brand Momentum."
    ),

    backstory=(
        "You specialize in recognizing patterns and highlighting events "
        "that require executive attention."
    ),

    llm=llm,
    verbose=True
)
