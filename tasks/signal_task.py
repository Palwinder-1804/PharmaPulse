from crewai import Task
from agents.signal_agent import signal_agent


signal_task = Task(
    description=(
        "You are given structured pharmaceutical events in JSON format:\n\n"
        "{scout_output}\n\n"

        "Your task is to classify each event into one strategic signal category.\n\n"

        "Valid Categories:\n"
        "- Competitive Threat\n"
        "- Market Opportunity\n"
        "- Pricing Shift\n"
        "- Regulatory Risk\n"
        "- Brand Momentum\n\n"

        "STRICT RULES:\n"
        "- Output STRICT JSON only.\n"
        "- Do NOT use markdown.\n"
        "- Do NOT add commentary outside JSON.\n"
        "- Do NOT re-write the event.\n"
        "- If output is not valid JSON, it will be rejected.\n\n"

        "Required Output Format:\n\n"

        "{\n"
        '  "signals": [\n'
        "    {\n"
        '      "event_id": 1,\n'
        '      "event_title": "string",\n'
        '      "category": "Competitive Threat | Market Opportunity | Pricing Shift | Regulatory Risk | Brand Momentum",\n'
        '      "impact_score": 1-10,\n'
        '      "confidence_score": 1-10,\n'
        '      "reason": "short explanation"\n'
        "    }\n"
        "  ]\n"
        "}\n"
    ),

    agent=signal_agent,

    expected_output="Valid JSON object containing classified strategic signals."
)
