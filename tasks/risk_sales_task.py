from crewai import Task
from agents.risk_sales_agent import risk_sales_agent


risk_sales_task = Task(
    description=(
        "Analyze competitive product landscape and generate structured "
        "risk assessment and sales momentum signals.\n\n"

        "STRICT RULES:\n"
        "- Output STRICT JSON only\n"
        "- No explanation\n"
        "- No markdown\n\n"

        "Required JSON Structure:\n\n"

        "{\n"
        '  "target_product": "string",\n'
        '  "risk_assessment": {\n'
        '    "regulatory_risk": "Low | Medium | High",\n'
        '    "pricing_pressure": "Low | Medium | High",\n'
        '    "competitive_threat": "Low | Medium | High"\n'
        "  },\n"
        '  "sales_momentum": {\n'
        '    "trend_direction": "Growing | Stable | Declining",\n'
        '    "growth_signal_strength": "Weak | Moderate | Strong"\n'
        "  },\n"
        '  "market_opportunity_score": "0-100",\n'
        '  "overall_risk_score": "0-100"\n'
        "}\n"
    ),

    expected_output=(
        "Strictly valid JSON with keys: target_product, risk_assessment, "
        "sales_momentum, market_opportunity_score, overall_risk_score. "
        "No text outside JSON."
    ),

    agent=risk_sales_agent
)
