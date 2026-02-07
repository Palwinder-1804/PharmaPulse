from crewai import Crew, Process

# -----------------------------
# Agents
# -----------------------------
from agents.product_scout_agent import product_scout_agent
from agents.risk_sales_agent import risk_sales_agent
from agents.usp_agent import usp_agent
from agents.strategy_agent import strategy_agent
from agents.product_supervisor_agent import product_supervisor_agent

# -----------------------------
# Tasks
# -----------------------------
from tasks.product_scout_task import product_scout_task
from tasks.risk_sales_task import risk_sales_task
from tasks.usp_task import usp_task
from tasks.strategy_task import strategy_task
from tasks.product_supervisor_task import product_supervisor_task

# -----------------------------
# Crew Definition
# -----------------------------
product_crew = Crew(
    agents=[
        product_scout_agent,
        risk_sales_agent,
        usp_agent,
        strategy_agent,
        product_supervisor_agent
    ],
    tasks=[
        product_scout_task,
        risk_sales_task,
        usp_task,
        strategy_task,
        product_supervisor_task
    ],
    process=Process.sequential,
    verbose=False,
    max_rpm=8
)
