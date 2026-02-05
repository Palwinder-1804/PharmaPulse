import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

llm = LLM(
   model="groq/llama-3.1-8b-instant",# ✅ Supported model
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
    max_tokens=900
)


