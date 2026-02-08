from market_crew import market_scout_crew, market_strategy_crew
from product_crew import product_crew
from services.json_storage import save_frontend_format

from services.search_service import (
    fetch_market_news,
    fetch_product_intelligence
)


# =====================================
# 🌍 MARKET INTELLIGENCE PIPELINE
# =====================================

def run_market_pipeline():

    external_news_data = fetch_market_news()

    # 1️⃣ Scout Crew
    scout_result = market_scout_crew.kickoff(
        inputs={"external_news_data": external_news_data}
    )

    scout_output = scout_result.tasks_output[0].raw

    # 2️⃣ Strategy Crew
    strategy_result = market_strategy_crew.kickoff(
        inputs={"scout_output": scout_output}
    )

    signal_output = strategy_result.tasks_output[0].raw
    insight_output = strategy_result.tasks_output[1].raw
    supervisor_output = strategy_result.tasks_output[2].raw

    # 🚨 DO NOT PARSE JSON HERE
    # Keep raw output and let json_storage extract properly

    return {
        "scout": scout_output,
        "signal": signal_output,
        "insight": insight_output,
        "supervisor": supervisor_output   # ← RAW
    }


# =====================================
# 💊 PRODUCT INTELLIGENCE PIPELINE
# =====================================

def run_product_pipeline(product_name: str):

    product_external_data = fetch_product_intelligence(product_name)

    result = product_crew.kickoff(
        inputs={
            "product_name": product_name,
            "external_product_data": product_external_data
        }
    )

    product_scout_output = result.tasks_output[0].raw
    risk_sales_output = result.tasks_output[1].raw
    usp_output = result.tasks_output[2].raw
    strategy_output = result.tasks_output[3].raw
    supervisor_output = result.tasks_output[4].raw

    # 🚨 DO NOT PARSE JSON HERE

    return {
        "product_name": product_name,
        "scout": product_scout_output,
        "risk_sales": risk_sales_output,
        "usp_analysis": usp_output,
        "strategy": strategy_output,
        "supervisor": supervisor_output   # ← RAW
    }


# =====================================
# 🚀 FULL INTELLIGENCE PIPELINE
# =====================================

def run_full_intelligence(product_name: str):

    market_data = run_market_pipeline()
    product_data = run_product_pipeline(product_name)

    # Save React-ready JSON (this will extract all JSON safely)
    file_path = save_frontend_format(
        market_data,
        product_data
    )

    print(f"\n💾 React-ready JSON saved to {file_path}")

    return {
        "market_intelligence": market_data,
        "product_intelligence": product_data
    }
