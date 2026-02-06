import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

# Scout model (lightweight)
scout_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
    max_tokens=400   #  reduce
)

#  Strategy models
strategic_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
    max_tokens=600   #  reduce
)
