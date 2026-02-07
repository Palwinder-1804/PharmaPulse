from tools.search_tool import market_search_tool, product_search_tool


# =====================================
# 🌍 MARKET SEARCH
# =====================================

def fetch_market_news():

    query = (
        "pharmaceutical industry news past 7 days "
        "major drug launches FDA approvals competitor expansions "
        "pricing disruptions mergers acquisitions"
    )

    results = market_search_tool.run(search_query=query)

    return str(results)[:3000]  # Token control


# =====================================
# 💊 PRODUCT SEARCH
# =====================================

def fetch_product_intelligence(product_name: str):

    query = (
        f"{product_name} pharmaceutical product "
        "competitors market share pricing strategy "
        "monthly sales performance USP unique selling proposition "
        "therapy area regulatory updates launch strategy"
    )

    results = product_search_tool.run(search_query=query)

    return str(results)[:4000]  # Product needs more data
