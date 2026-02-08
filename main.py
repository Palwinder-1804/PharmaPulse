from run_pipeline import run_full_intelligence
import json


if __name__ == "__main__":

    print("\n======================================")
    print("🚀 PHARMA INTELLIGENCE ENGINE STARTED")
    print("======================================\n")

    product_name = input("Enter target pharmaceutical product name: ")

    print("\n🔄 Running Full Intelligence Pipeline...\n")

    final_output = run_full_intelligence(product_name)

    # ========================================
    # PRINT MARKET INTELLIGENCE
    # ========================================

    print("\n======================================")
    print("🌍 MARKET INTELLIGENCE")
    print("======================================\n")

    market_data = final_output["market_intelligence"]

    print("📰 Scout Output:\n")
    print(market_data["scout"])

    print("\n📊 Signal Analysis:\n")
    print(market_data["signal"])

    print("\n📈 Strategic Insights:\n")
    print(market_data["insight"])

    print("\n🧠 Market Supervisor Summary:\n")
    print(json.dumps(market_data["supervisor"], indent=2))


    # ========================================
    # PRINT PRODUCT INTELLIGENCE
    # ========================================

    print("\n======================================")
    print("PRODUCT INTELLIGENCE")
    print("======================================\n")

    product_data = final_output["product_intelligence"]

    print(f"Target Product: {product_name}\n")

    print(" Product Scout:\n")
    print(product_data["scout"])

    print("\nRisk & Sales Monitoring:\n")
    print(product_data["risk_sales"])

    print("\n USP Analysis:\n")
    print(product_data["usp_analysis"])

    print("\n Strategy Recommendation:\n")
    print(product_data["strategy"])

    print("\nProduct Supervisor Summary:\n")
    print(json.dumps(product_data["supervisor"], indent=2))


    print("\n======================================")
    print(" INTELLIGENCE RUN COMPLETE")
    print("======================================\n")
