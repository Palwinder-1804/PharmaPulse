from crewai import Crew, Process

from agents.scout_agent import scout_agent
from agents.signal_agent import signal_agent
from agents.insight_agent import insight_agent
from agents.supervisor_agent import supervisor_agent

from tasks.scouting_task import scouting_task
from tasks.signal_task import signal_task
from tasks.insight_task import insight_task
from tasks.supervisor_task import supervisor_task


# ===============================
# 🔎 MARKET SCOUT CREW (15 min)
# ===============================

market_scout_crew = Crew(
    agents=[scout_agent],
    tasks=[scouting_task],
    process=Process.sequential,
    verbose=False,
    max_rpm=8
)


# ===============================
# 📊 MARKET STRATEGY CREW (6 hr)
# ===============================

market_strategy_crew = Crew(
    agents=[
        signal_agent,
        insight_agent,
        supervisor_agent
    ],
    tasks=[
        signal_task,
        insight_task,
        supervisor_task
    ],
    process=Process.sequential,
    verbose=False,
    max_rpm=8
)
