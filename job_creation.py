import os
import requests

url = f"https://{os.getenv('DATABRICKS_HOST')}/api/2.0/jobs/create"

def create_job(job_name:str, cluster_id:str, notebook_path:str):

    token = os.getenv("DATABRICKS_TOKEN")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "email_notifications": {
            "on_failure": os.getenv("CREATOR_EMAIL"),
            "on_success": os.getenv("CREATOR_EMAIL")
        },
        "format": "MULTI_TASK",
        "max_concurrent_runs": 1,
        "name": f"{job_name}",
        "notification_settings": {
            "alert_on_last_attempt": False,
            "no_alert_for_canceled_runs": False,
            "no_alert_for_skipped_runs": False
        },
        "run_as": {
            "user_name": os.getenv("WORKSPACE_EMAIL")
        },
        "tasks": [
            {
            "existing_cluster_id": f"{cluster_id}",
            "notebook_task": {
                "notebook_path": f"{notebook_path}",
                "source": "WORKSPACE"
            },
            "run_if": "ALL_SUCCESS",
            "task_key": "fact_arrivals_gold_task"
            }
        ]
    }

    return headers, data

headers, json = create_job("hrynchuk_lab10_job", "0420-150638-dy9ru7jm", f'/Users/{os.getenv("WORKSPACE_EMAIL")}/lab10/test_notebook')

response = requests.post(url, headers=headers, json=json)

print(response.status_code)
print(response.json())

