from crewai import Task
from agents.scout_agent import scout_agent


scouting_task = Task(
    description=(
        "You are provided with structured pharmaceutical news data:\n\n"
        "{external_news_data}\n\n"

        "Analyze ONLY this data and extract the TOP 5 most strategically "
        "significant pharmaceutical events from the past 7 days.\n\n"

        "STRICT RULES:\n"
        "- Do NOT call any search tool.\n"
        "- Do NOT generate new queries.\n"
        "- Do NOT fabricate information.\n"
        "- Only analyze the provided data.\n"
        "- Ignore low-impact news.\n"
        "- Output STRICT JSON only.\n"
        "- If output is not valid JSON, it will be rejected.\n"
        "- Do NOT use markdown.\n"
        "- Do NOT add commentary outside JSON.\n\n"

        "Required Output Format:\n\n"

        "{\n"
        '  "events": [\n'
        "    {\n"
        '      "event_id": 1,\n'
        '      "title": "string",\n'
        '      "companies": ["string"],\n'
        '      "therapy_area": "string",\n'
        '      "event_type": "Drug Launch | FDA Approval | M&A | Pricing | Expansion",\n'
        '      "summary": "max 40 words",\n'
        '      "strategic_impact": "short explanation",\n'
        '      "importance_score": 1-10\n'
        "    }\n"
        "  ]\n"
        "}\n"
    ),

    agent=scout_agent,

    expected_output="Valid JSON object containing top 5 strategic pharmaceutical events."
)
