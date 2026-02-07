from crewai import Task
from agents.usp_agent import usp_agent
from tasks.product_scout_task import product_scout_task


usp_task = Task(
    description=(
        "Using the product scouting results from the previous task, "
        "analyze competitive positioning and identify key USPs.\n\n"

        "Return STRICT JSON only.\n"
        "No markdown. No explanation outside JSON.\n\n"

        "Required Output Format:\n\n"

        "{\n"
        '  "usp_analysis": [\n'
        "    {\n"
        '      "product_name": "string",\n'
        '      "unique_selling_points": ["string"],\n'
        '      "why_sales_are_strong": "string",\n'
        '      "innovation_factor": "string"\n'
        "    }\n"
        "  ]\n"
        "}\n"
    ),

    agent=usp_agent,

    context=[product_scout_task],   # 🔥 THIS IS IMPORTANT

    expected_output=(
        "Strictly valid JSON with key: usp_analysis (array). "
        "Each item must include: product_name, unique_selling_points (array), "
        "why_sales_are_strong, innovation_factor. "
        "No explanation. JSON only."
    ),
)
