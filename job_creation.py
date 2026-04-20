import os
import requests

url = "https://adb-7405605185991044.4.azuredatabricks.net/api/2.0/jobs/create"

token = os.getenv("PERSONAL_ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

data = {
    "email_notifications": {
        "on_failure": [os.getenv("CREATOR_EMAIL")],
        "on_success": [os.getenv("CREATOR_EMAIL")]
    },
    "format": "MULTI_TASK",
    "max_concurrent_runs": 1,
    "name": "hrynchuk_lab10_job",
    "notification_settings": {
        "alert_on_last_attempt": False,
        "no_alert_for_canceled_runs": False,
        "no_alert_for_skipped_runs": False
    },
    "run_as": {
        "user_name": [os.getenv("CREATOR_EMAIL")]
    },
    "tasks": [
        {
        "existing_cluster_id": "0420-150638-dy9ru7jm",
        "notebook_task": {
            "notebook_path": f"Users/{[os.getenv("WORKSPACE_EMAIL")]}/lab10/test_notebook",
            "source": "WORKSPACE"
        },
        "run_if": "ALL_SUCCESS",
        "task_key": "fact_arrivals_gold_task"
        }
    ]

}

