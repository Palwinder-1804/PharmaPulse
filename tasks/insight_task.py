from crewai import Task
from agents.insight_agent import insight_agent
from tasks.signal_task import signal_task


insight_task = Task(
    description=(
        "Using the classified strategic signals from the previous task, "
        "generate board-level strategic intelligence.\n\n"

        "IMPORTANT RULES:\n"
        "- Output STRICT JSON only.\n"
        "- Do NOT use markdown.\n"
        "- Do NOT add explanations outside JSON.\n"
        "- If output is not valid JSON, it will be rejected.\n\n"

        "Required Output Format:\n\n"

        "{\n"
        '  "market_trend": "string",\n'
        '  "threat_level": "Low | Medium | High",\n'
        '  "opportunity_areas": ["string"],\n'
        '  "competitive_pressure_score": 1-10,\n'
        '  "recommended_moves": ["string"],\n'
        '  "strategic_summary": "short executive-level explanation"\n'
        "}\n"
    ),

    agent=insight_agent,

    context=[signal_task],

    expected_output="Valid JSON object containing strategic intelligence."
)
