from crewai import Task
from agents.supervisor_agent import supervisor_agent
from tasks.insight_task import insight_task


supervisor_task = Task(
    description=(
        "Using the structured strategic intelligence generated in the previous task, "
        "generate final executive summary.\n\n"

        "STRICT RULES:\n"
        "- Output STRICT JSON only.\n"
        "- No markdown.\n"
        "- No commentary outside JSON.\n\n"

        "Required Output Format:\n\n"

        "{\n"
        '  "overall_market_condition": "string",\n'
        '  "top_priority": "string",\n'
        '  "risk_index": 1-10,\n'
        '  "capital_allocation_focus": ["string"],\n'
        '  "immediate_actions": ["string"],\n'
        '  "executive_summary": "short high-level conclusion"\n'
        "}\n"
    ),

    agent=supervisor_agent,

    context=[insight_task],

    expected_output="Valid JSON executive summary."
)
