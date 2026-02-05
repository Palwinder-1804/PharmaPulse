from crewai import Task
from agents.insight_agent import insight_agent


insight_task = Task(
    description=(
        "Analyze the provided pharma events and convert them into "
        "BOARDROOM-LEVEL strategic intelligence.\n\n"

        "Focus on:\n"
        "- Competitive advantage shifts\n"
        "- Market risks\n"
        "- Revenue opportunities\n"
        "- Industry disruption\n\n"

        "⚠️ STRICT OUTPUT FORMAT:\n\n"

        "🚨 Strategic Insight:\n"
        "(1–2 powerful sentences)\n\n"

        "📊 Market Implication:\n"
        "(Explain what this means for the industry)\n\n"

        "⚠️ Risk Level:\n"
        "Low / Medium / High\n\n"

        "✅ Recommended Action:\n"
        "(What should leadership do?)\n\n"

        "Repeat for each major event."
    ),

    agent=insight_agent,

    expected_output="Executive-ready pharma intelligence report.",
)
