# import json

# with open("frontend_intelligence.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

# print(data)
# print(data["market_intelligence"])


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# ✅ Allow React app origin
origins = [
    "http://localhost:5173",  # Vite React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 🔥 Allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/intelligence")
def get_intelligence():
    with open("frontend_intelligence.json", "r", encoding="utf-8") as f:
        return json.load(f)