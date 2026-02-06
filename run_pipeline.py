from crew import pharma_crew
from tools.search_tool import search_tool


def run_pipeline():

    # Correct way to call Serper tool
    search_results = search_tool.run(
        search_query="pharmaceutical industry news past 7 days "
                     "major drug launches FDA approvals competitor expansions "
                     "pricing disruptions mergers acquisitions"
    )

    search_results = str(search_results)[:2500]


    result = pharma_crew.kickoff(
        inputs={
            "external_news_data": search_results
        }
    )

    return {
        "scout": result.tasks_output[0].raw,
        "signal": result.tasks_output[1].raw,
        "insight": result.tasks_output[2].raw,
        "supervisor": result.tasks_output[3].raw
    }
