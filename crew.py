from crewai import Crew, Process

from agents.scout_agent import scout_agent
from agents.signal_agent import signal_agent
from agents.insight_agent import insight_agent

from tasks.scouting_task import scouting_task
from tasks.signal_task import signal_task
from tasks.insight_task import insight_task


pharma_crew = Crew(
    agents=[
        scout_agent,
        signal_agent,
        insight_agent
    ],

    tasks=[
        scouting_task,
        signal_task,
        insight_task
    ],

    process=Process.sequential,  # jaruri hai ye laadle
    verbose=True,
    max_rpm=8 #gareeb hu api limit hojati h 
    
)
