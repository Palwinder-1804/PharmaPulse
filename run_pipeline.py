import time
from crew import scout_crew, strategy_crew
from tools.search_tool import search_tool

cache = {
    "scout": None,
    "signal": None,
    "insight": None,
    "supervisor": None,
    "scout_time": 0,
    "strategic_time": 0
}

SCOUT_INTERVAL = 15 * 60
STRATEGIC_INTERVAL = 6 * 60 * 60


def run_pipeline(force=False):

    current_time = time.time()

    # ===============================
    # 1️⃣ SCOUT (15 min)
    # ===============================
    if (
        force
        or cache["scout"] is None
        or current_time - cache["scout_time"] > SCOUT_INTERVAL
    ):

        print("🔄 Running Scout Crew...")

        search_results = search_tool.run(
            search_query=(
                "pharmaceutical industry news past 7 days "
                "major drug launches FDA approvals competitor expansions "
                "pricing disruptions mergers acquisitions"
            )
        )

        cleaned = str(search_results)[:2500]

        result = scout_crew.kickoff(
            inputs={"external_news_data": cleaned}
        )

        cache["scout"] = result.tasks_output[0].raw
        cache["scout_time"] = current_time

    # ===============================
    # 2️⃣ STRATEGY (6 hr)
    # ===============================
    if (
        force
        or cache["strategic_time"] == 0
        or current_time - cache["strategic_time"] > STRATEGIC_INTERVAL
    ):

        print("🧠 Running Strategy Crew...")

        result = strategy_crew.kickoff(
            inputs={"scout_output": cache["scout"]}
        )

        cache["signal"] = result.tasks_output[0].raw
        cache["insight"] = result.tasks_output[1].raw
        cache["supervisor"] = result.tasks_output[2].raw
        cache["strategic_time"] = current_time

    return cache
