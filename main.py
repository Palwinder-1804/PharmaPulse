from run_pipeline import (
    run_market_pipeline,
    run_product_pipeline,
    run_full_intelligence
)
import json


if __name__ == "__main__":

    print("\n======================================")
    print("🚀 PHARMA INTELLIGENCE ENGINE STARTED")
    print("======================================\n")

    # 🔹 Ask for product name
    product_name = input("Enter target pharmaceutical product name: ")

    print("\n🔄 Running Market Intelligence...\n")
    market_data = run_market_pipeline()

    print("🔄 Running Product Intelligence...\n")
    product_data = run_product_pipeline(product_name)

    # ========================================
    # PRINT RESULTS
    # ========================================

    print("\n======================================")
    print("🌍 MARKET INTELLIGENCE")
    print("======================================\n")

    print("📰 Scout Output:\n")
    print(market_data["market"]["scout"])

    print("\n📊 Signal Analysis:\n")
    print(market_data["market"]["signal"])

    print("\n📈 Strategic Insights:\n")
    print(market_data["market"]["insight"])

    print("\n🧠 Market Supervisor Summary:\n")
    print(json.dumps(market_data["market"]["supervisor"], indent=2))


    print("\n======================================")
    print("💊 PRODUCT INTELLIGENCE")
    print("======================================\n")

    print(f"🔎 Target Product: {product_name}\n")

    print("📌 Product Scout:\n")
    print(product_data["product"]["scout"])

    print("\n⚠ Risk & Sales Monitoring:\n")
    print(product_data["product"]["risk_sales"])

    print("\n✨ USP Analysis:\n")
    print(product_data["product"]["usp_analysis"])

    print("\n🚀 Strategy Recommendation:\n")
    print(product_data["product"]["strategy"])

    print("\n🧠 Product Supervisor Summary:\n")
    print(json.dumps(product_data["product"]["supervisor"], indent=2))

    print("\n======================================")
    print("✅ INTELLIGENCE RUN COMPLETE")
    print("======================================\n")
