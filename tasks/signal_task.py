from crewai import Task
from agents.signal_agent import signal_agent

signal_task = Task(
    description=(
        "Analyze the scouting report and classify each event into one of the following:\n"
        "- Competitive Threat\n"
        "- Market Opportunity\n"
        "- Pricing Shift\n"
        "- Regulatory Risk\n"
        "- Brand Momentum\n\n"
        "Explain WHY each signal is strategically important."
    ),

    agent=signal_agent,
    expected_output="A classified list of strategic signals."
)
