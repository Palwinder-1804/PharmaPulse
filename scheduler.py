from apscheduler.schedulers.background import BackgroundScheduler
from run_pipeline import run_full_intelligence

scheduler = BackgroundScheduler()
scheduler.start()

active_jobs = {}

def schedule_product_refresh(product_name: str):

    job_id = f"{product_name}_job"

    # Remove old job if exists
    if job_id in active_jobs:
        scheduler.remove_job(job_id)

    # Schedule every 15 minutes
    scheduler.add_job(
        run_full_intelligence,
        "interval",
        minutes=15,
        args=[product_name],
        id=job_id,
        replace_existing=True
    )

    active_jobs[job_id] = product_name

    print(f"✅ Scheduled auto-refresh for {product_name} every 15 minutes")
