from crewai import Task
from agents.competitive_agent import competitive_agent


competitive_task = Task(
    description=(
        "You are given structured pharmaceutical events:\n\n"
        "{scout_output}\n\n"

        "Identify competitor positioning and product USPs.\n\n"

        "STRICT RULES:\n"
        "- Output STRICT JSON only.\n"
        "- No markdown.\n"
        "- No commentary outside JSON.\n\n"

        "Required Output Format:\n\n"

        "{\n"
        '  "competitor_analysis": [\n'
        "    {\n"
        '      "company": "string",\n'
        '      "product_focus": "string",\n'
        '      "unique_selling_proposition": "string",\n'
        '      "market_strategy": "string",\n'
        '      "pricing_strategy": "string",\n'
        '      "innovation_focus": "string"\n'
        "    }\n"
        "  ]\n"
        "}\n"
    ),

    agent=competitive_agent,
    expected_output="Valid JSON competitor intelligence."
)
