from crewai import Task
from agents.product_supervisor_agent import product_supervisor_agent
from tasks.strategy_task import strategy_task


product_supervisor_task = Task(
    description=(
        "Using the complete product intelligence analysis generated in the previous steps, "
        "consolidate everything into a FINAL EXECUTIVE PRODUCT INTELLIGENCE REPORT.\n\n"

        "⚠️ STRICT OUTPUT: Return ONLY valid JSON.\n\n"

        "{\n"
        "  \"product_name\": \"\",\n"
        "  \"overall_product_risk\": \"Low | Medium | High\",\n"
        "  \"market_position\": \"Leader | Challenger | Niche | Declining\",\n"
        "  \"core_competitors\": [],\n"
        "  \"monthly_sales_outlook\": \"Growing | Stable | Declining\",\n"
        "  \"strongest_usp\": \"\",\n"
        "  \"biggest_risk_factor\": \"\",\n"
        "  \"launch_strategy_recommendation\": \"\",\n"
        "  \"existing_product_strategy_update\": \"\",\n"
        "  \"executive_summary\": \"2-3 powerful sentences\"\n"
        "}\n\n"

        "Return ONLY JSON. No explanation."
    ),

    agent=product_supervisor_agent,

    context=[strategy_task],   # 🔥 This replaces all template placeholders

    expected_output="Final structured product intelligence JSON."
)
