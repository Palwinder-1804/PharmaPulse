from crewai import LLM

# ==============================
# SCOUT MODEL (Lightweight)
# ==============================

scout_llm = LLM(
    model="ollama/phi3:mini",
    base_url="http://localhost:11434",
    temperature=0,
    max_tokens=400
)
from crewai import LLM


# =================================
# 🔎 SCOUT MODEL (Fast + Deterministic)
# =================================

scout_llm = LLM(
    model="ollama/phi3:mini",
    base_url="http://localhost:11434",
    temperature=0,
    top_p=0.9,
    max_tokens=300,
    request_timeout=120
)


# =================================
# 📊 STRATEGIC MODEL (Balanced Reasoning)
# =================================

strategic_llm = LLM(
    model="ollama/phi3:mini",
    base_url="http://localhost:11434",
    temperature=0.2,
    top_p=0.9,
    max_tokens=500,
    request_timeout=120
)


# =================================
# 🎯 SUPERVISOR MODEL (JSON Focused)
# =================================

supervisor_llm = LLM(
    model="ollama/phi3:mini",
    base_url="http://localhost:11434",
    temperature=0,
    top_p=0.8,
    max_tokens=400,
    request_timeout=120
)

# ==============================
# STRATEGIC MODEL
# ==============================

strategic_llm = LLM(
    model="ollama/phi3:mini",
    base_url="http://localhost:11434",
    temperature=0.2,
    max_tokens=600
)
