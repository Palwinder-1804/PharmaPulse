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

# ==============================
# STRATEGIC MODEL
# ==============================

strategic_llm = LLM(
    model="ollama/phi3:mini",
    base_url="http://localhost:11434",
    temperature=0.2,
    max_tokens=600
)
