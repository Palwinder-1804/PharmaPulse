from run_pipeline import run_full_intelligence
import json

if __name__ == "__main__":

    print("\n======================================")
    print("🚀 PHARMA INTELLIGENCE ENGINE STARTED")
    print("======================================\n")

    product_name = input("Enter target pharmaceutical product name: ")

    # 🔥 Run FULL pipeline (this automatically saves JSON)
    final_output = run_full_intelligence(product_name)

    print("\n======================================")
    print("✅ INTELLIGENCE SAVED TO data/frontend_intelligence.json")
    print("======================================\n")
