from crew import pharma_crew

def run_pipeline():
    result = pharma_crew.kickoff()

    return {
        "scout": result.tasks_output[0].raw,
        "signal": result.tasks_output[1].raw,
        "insight": result.tasks_output[2].raw,
        "supervisor": result.tasks_output[3].raw
    }
