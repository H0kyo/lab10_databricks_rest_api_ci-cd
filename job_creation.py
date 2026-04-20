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
}

