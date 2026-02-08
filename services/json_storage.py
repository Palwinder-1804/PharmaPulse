import json
import os
import re
from datetime import datetime
import spacy

DATA_DIR = "data"
FRONTEND_FILE = os.path.join(DATA_DIR, "frontend_intelligence.json")

# ------------------------------
# Load NLP model safely
# ------------------------------
try:
    nlp = spacy.load("en_core_web_sm")
except:
    raise Exception(
        "SpaCy model not found. Run: python -m spacy download en_core_web_sm"
    )


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
    if not text:
        return {}

    text = text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(text)
    except:
        pass

    possible_json_blocks = re.findall(r"\{[\s\S]*?\}", text)

    for block in possible_json_blocks:
        try:
            return json.loads(block)
        except:
            continue

    return {}


# =========================================
# SMART COMPANY EXTRACTION
# =========================================
def extract_companies_from_text(text):
    if not text:
        return []

    doc = nlp(text)
    companies = []

    for ent in doc.ents:
        if ent.label_ == "ORG":
            cleaned = ent.text.strip()

            # Remove obvious noise
            if len(cleaned) < 3:
                continue
            if cleaned.lower() in ["fda", "ema", "who"]:
                continue

            companies.append(cleaned)

    return list(set(companies))


# =========================================
# EVENT TYPE DETECTOR
# =========================================
def detect_event_type(text):
    text = text.lower()

    mapping = {
        "FDA Approval": ["fda approval", "approved by fda"],
        "Drug Launch": ["launches", "introduces", "rollout"],
        "M&A": ["acquires", "acquisition", "merger"],
        "Pricing": ["price increase", "pricing strategy"],
        "Expansion": ["expands", "new facility", "expansion"]
    }

    for event, keywords in mapping.items():
        for keyword in keywords:
            if keyword in text:
                return event

    return "Market Update"


# =========================================
# AUTO SIGNAL GENERATOR
# =========================================
def generate_signal(event_type):

    mapping = {
        "FDA Approval": {
            "signal_strength": "High",
            "impact_score": 85,
            "market_impact": "Bullish",
            "competitor_pressure": "High",
            "time_horizon": "Short to Medium Term"
        },
        "Drug Launch": {
            "signal_strength": "High",
            "impact_score": 75,
            "market_impact": "Positive",
            "competitor_pressure": "Medium",
            "time_horizon": "Medium Term"
        },
        "M&A": {
            "signal_strength": "Very High",
            "impact_score": 95,
            "market_impact": "Transformational",
            "competitor_pressure": "High",
            "time_horizon": "Long Term"
        }
    }

    return mapping.get(event_type, {
        "signal_strength": "Medium",
        "impact_score": 50,
        "market_impact": "Neutral",
        "competitor_pressure": "Low",
        "time_horizon": "Short Term"
    })


# =========================================
# MAIN SAVE FUNCTION
# =========================================
def save_frontend_format(market_data, product_data):

    ensure_data_folder()

    raw_scout_text = market_data.get("scout", "")
    raw_signal_text = market_data.get("signal", "")
    raw_article_text = market_data.get("raw_article_text", "")
    raw_insight = market_data.get("insight", "")
    raw_supervisor = market_data.get("supervisor", "")

    scout_output = extract_json(raw_scout_text) or {}
    signal_analysis = extract_json(raw_signal_text) or {}

    combined_text = f"{raw_article_text} {raw_scout_text}"

    # --------------------------------------------------
    # SELF-HEALING INTELLIGENCE LOGIC
    # --------------------------------------------------

    # Ensure companies
    if not scout_output.get("companies"):
        scout_output["companies"] = extract_companies_from_text(combined_text)

    # Ensure event type
    if not scout_output.get("event_type"):
        scout_output["event_type"] = detect_event_type(combined_text)

    # Ensure signal
    if not signal_analysis:
        signal_analysis = generate_signal(
            scout_output.get("event_type")
        )

    # Add metadata
    scout_output["processed_at"] = datetime.utcnow().isoformat()
    scout_output["company_count"] = len(scout_output.get("companies", []))

    clean_market = {
        "scout_output": scout_output,
        "signal_analysis": signal_analysis,
        "strategic_insights": extract_json(raw_insight),
        "market_supervisor_summary": (
            extract_json(raw_supervisor.get("raw_output", ""))
            if isinstance(raw_supervisor, dict)
            else extract_json(raw_supervisor)
        ),
    }

    # --------------------------------------------------
    # LOAD EXISTING FILE SAFELY
    # --------------------------------------------------
    if os.path.exists(FRONTEND_FILE):
        try:
            with open(FRONTEND_FILE, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        except:
            existing_data = {}
    else:
        existing_data = {}

    existing_data.setdefault("market_intelligence", {})
    existing_data.setdefault("productIntelligence", [])
    existing_data.setdefault("finalExecutiveProductIntelligenceReport", [])

    existing_data["market_intelligence"] = clean_market

    # --------------------------------------------------
    # SAVE
    # --------------------------------------------------
    with open(FRONTEND_FILE, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, indent=4)

    print("✅ Market intelligence saved successfully.")
    return FRONTEND_FILE
