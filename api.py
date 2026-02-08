from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

from run_pipeline import run_full_intelligence
from scheduler import schedule_product_refresh

app = FastAPI()

DATA_FILE = "data/frontend_intelligence.json"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------
# GET INTELLIGENCE DATA
# ----------------------------------

@app.get("/intelligence")
def get_intelligence():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"message": "No data available"}


# ----------------------------------
# RUN PRODUCT + SCHEDULE REFRESH
# ----------------------------------

@app.post("/run/{product_name}")
def run_product(product_name: str):

    # Run immediately
    run_full_intelligence(product_name)

    # Schedule 15 min refresh
    schedule_product_refresh(product_name)

    return {
        "message": f"{product_name} intelligence started",
        "auto_refresh": "Every 15 minutes"
    }
