from crewai import Task
from agents.strategy_agent import strategy_agent
from tasks.usp_task import usp_task


strategy_task = Task(
    description=(
        "Using the complete product intelligence analysis generated in the previous steps, "
        "develop a comprehensive pharmaceutical market strategy.\n\n"

        "Focus on:\n"
        "- Launch pricing optimization\n"
        "- Competitive positioning\n"
        "- Target segment prioritization\n"
        "- Partnership strategy\n"
        "- Defensive moves for existing products\n\n"

        "STRICT RULES:\n"
        "- Output STRICT JSON only\n"
        "- No markdown\n"
        "- No commentary outside JSON\n\n"

        "Required Output Format:\n\n"

        "{\n"
        '  "new_product_launch_strategy": {\n'
        '      "pricing_strategy": "string",\n'
        '      "positioning_strategy": "string",\n'
        '      "target_segment": "string",\n'
        '      "partnership_recommendation": "string"\n'
        "  },\n"
        '  "existing_product_market_strategy": {\n'
        '      "defensive_moves": ["string"],\n'
        '      "pricing_adjustment": "string",\n'
        '      "marketing_focus": "string"\n'
        "  }\n"
        "}\n"
    ),

    agent=strategy_agent,

    context=[usp_task],   # 🔥 This replaces all template placeholders

    expected_output=(
        "Strictly valid JSON with two top-level keys: "
        "new_product_launch_strategy and existing_product_market_strategy. "
        "Each must follow the defined structure exactly. "
        "No explanations. JSON only."
    ),
)
