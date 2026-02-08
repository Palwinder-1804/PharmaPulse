import json
import os
import re
from datetime import datetime

DATA_DIR = "data"
FRONTEND_FILE = os.path.join(DATA_DIR, "frontend_intelligence.json")


# =========================================
# ENSURE DATA FOLDER
# =========================================

def ensure_data_folder():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


# =========================================
# ROBUST JSON EXTRACTOR
# =========================================

def extract_json(text):
    """
    Extracts the FIRST valid JSON object from messy LLM output.
    Handles:
    - Markdown ```json blocks
    - Multiple JSON objects
    - Extra text before/after JSON
    """

    if not text:
        return {}

    # Remove markdown wrappers
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    # Find all possible JSON blocks (non-greedy)
    possible_json_blocks = re.findall(r"\{[\s\S]*?\}", text)

    for block in possible_json_blocks:
        try:
            return json.loads(block)
        except:
            continue

    return {}


# =========================================
# MAIN SAVE FUNCTION
# =========================================

def save_frontend_format(market_data, product_data):

    ensure_data_folder()

    # -------------------------------
    # CLEAN MARKET
    # -------------------------------

    clean_market = {
        "scout_output": extract_json(market_data.get("scout", "")),
        "signal_analysis": extract_json(market_data.get("signal", "")),
        "strategic_insights": extract_json(market_data.get("insight", "")),
        "market_supervisor_summary": (
            extract_json(market_data.get("supervisor", {}).get("raw_output", ""))
            if isinstance(market_data.get("supervisor"), dict)
            else extract_json(market_data.get("supervisor", ""))
        )
    }

    # -------------------------------
    # CLEAN PRODUCT
    # -------------------------------

    clean_product = {
        "target_product": product_data.get("product_name"),
        "product_scout": extract_json(product_data.get("scout", "")),
        "risk_and_sales_monitoring": extract_json(product_data.get("risk_sales", "")),
        "usp_analysis": extract_json(product_data.get("usp_analysis", "")),
        "strategy_recommendation": extract_json(product_data.get("strategy", ""))
    }

    clean_final_report = (
        extract_json(product_data.get("supervisor", {}).get("raw_output", ""))
        if isinstance(product_data.get("supervisor"), dict)
        else extract_json(product_data.get("supervisor", ""))
    )

    # -------------------------------
    # LOAD EXISTING FILE
    # -------------------------------

    if os.path.exists(FRONTEND_FILE):
        with open(FRONTEND_FILE, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
    else:
        existing_data = {
            "market_intelligence": {},
            "productIntelligence": [],
            "finalExecutiveProductIntelligenceReport": []
        }

    # -------------------------------
    # UPDATE MARKET
    # -------------------------------

    existing_data["market_intelligence"] = clean_market

    # -------------------------------
    # APPEND PRODUCT HISTORY
    # -------------------------------

    if clean_product["target_product"]:
        existing_data["productIntelligence"].append(clean_product)

    if clean_final_report:
        existing_data["finalExecutiveProductIntelligenceReport"].append(
            clean_final_report
        )

    # -------------------------------
    # SAVE FILE
    # -------------------------------

    with open(FRONTEND_FILE, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, indent=4)

    return FRONTEND_FILE
