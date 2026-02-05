from crewai import Task
from agents.supervisor_agent import supervisor_agent

supervisor_task = Task(
    description=(
        "Review the outputs from Scouting, Signal Classification, "
        "and Strategic Insight.\n\n"

        "Produce a FINAL EXECUTIVE BRIEF in this STRICT FORMAT:\n\n"

        "🔎 Overall Market Condition:\n"
        "(2-3 sentences summarizing global pharma landscape)\n\n"

        "🚨 Top Strategic Priority:\n"
        "(Most critical risk or opportunity)\n\n"

        "📊 Risk Concentration:\n"
        "(Low / Medium / High overall market risk)\n\n"

        "🎯 Immediate Executive Action:\n"
        "(Clear directive for leadership)\n\n"

        "Keep it concise and boardroom-ready."
    ),

    agent=supervisor_agent,
    expected_output="Consolidated executive briefing."
)
