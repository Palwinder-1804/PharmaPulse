import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()
#groq specify krna mt bhulna vrna ni chalega
llm = LLM(
    model="groq/mixtral-8x7b",  
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
    max_tokens=900
)
