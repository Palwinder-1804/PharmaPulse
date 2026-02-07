from crewai import Task
from agents.product_scout_agent import product_scout_agent


product_scout_task = Task(
    description=(
        "Target Product Information:\n\n"
        "{product_name}\n\n"

        "Identify similar products in the same therapy area and region.\n\n"

        "STRICT RULES:\n"
        "- Output STRICT JSON only.\n"
        "- Do not add commentary outside JSON.\n"
        "- Do not use markdown formatting.\n\n"

        "Required Output Format:\n\n"

        "{\n"
        '  "target_product": "string",\n'
        '  "similar_products": [\n'
        "    {\n"
        '      "product_name": "string",\n'
        '      "company": "string",\n'
        '      "therapy_area": "string",\n'
        '      "approval_status": "Approved | Phase III | Phase II",\n'
        '      "estimated_market_share": "string",\n'
        '      "pricing_position": "Premium | Competitive | Low Cost"\n'
        "    }\n"
        "  ]\n"
        "}\n"
    ),

    expected_output=(
        "Return strictly valid JSON with the following keys: "
        "target_product (string) and similar_products (array of objects). "
        "Each similar product must include: "
        "product_name, company, therapy_area, approval_status, "
        "estimated_market_share, pricing_position. "
        "No explanation. No markdown. JSON only."
    ),

    agent=product_scout_agent
)
