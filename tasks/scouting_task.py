from crewai import Task
from agents.scout_agent import scout_agent


scouting_task = Task(
    description=(
        "You are provided with external pharmaceutical news data below:\n\n"
        "{external_news_data}\n\n"

        "Your job is to analyze this data and identify ONLY the MOST "
        "strategically significant pharmaceutical events from the past 7 days.\n\n"

        "🔴 STRICT RULES:\n"
        "- Do NOT attempt to call any search tool.\n"
        "- Do NOT generate new search queries.\n"
        "- Do NOT fabricate information.\n"
        "- Only analyze the provided news data.\n"
        "- Ignore low-impact or irrelevant news.\n\n"

        "🎯 Focus Areas:\n"
        "- Major drug launches\n"
        "- Competitor expansions\n"
        "- Pricing disruptions\n"
        "- FDA / regulatory approvals\n"
        "- Mergers & acquisitions\n\n"

        "Return ONLY the TOP 5 events with the HIGHEST strategic importance.\n\n"

        "⚠️ STRICT OUTPUT FORMAT:\n\n"

        "Event 1:\n"
        "Title:\n"
        "Summary (MAX 2 lines, under 40 words):\n"
        "Companies Involved:\n"
        "Therapy Area:\n"
        "Strategic Impact:\n\n"

        "Repeat for Event 2–5."
    ),

    agent=scout_agent,

    expected_output="A structured list of the top 5 strategic pharma events.",
)
