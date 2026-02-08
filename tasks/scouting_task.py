from crewai import Task
from agents.scout_agent import scout_agent


scouting_task = Task(
    description=(
        "You are given structured pharmaceutical market news data:\n\n"
        "{external_news_data}\n\n"

        "Your job is to extract the TOP 5 most strategically significant events.\n\n"

        "STRICT EXECUTION RULES:\n"
        "1. DO NOT call any tools.\n"
        "2. DO NOT generate new queries.\n"
        "3. DO NOT fabricate information.\n"
        "4. Use ONLY the provided data.\n"
        "5. Return STRICT VALID JSON.\n"
        "6. No markdown.\n"
        "7. No commentary.\n"
        "8. No reasoning.\n"
        "9. Output must start with '{' and end with '}'.\n"
        "10. If no events found, return empty array.\n\n"

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
        '      "importance_score": 1\n'
        "    }\n"
        "  ]\n"
        "}\n"
    ),

    agent=scout_agent,

    expected_output="Strict valid JSON containing an events array."
)
