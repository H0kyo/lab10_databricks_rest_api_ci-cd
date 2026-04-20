import os
import requests

url = "https://adb-7405605185991044.4.azuredatabricks.net/api/2.0/clusters/create"

token = os.getenv("DATABRICKS_TOKEN")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

data = {
    "cluster_name": "hrynchuk_lab10_cluster",
    "spark_version": "14.3.x-scala2.12",
    "node_type_id": "Standard_DS3_v2",
    "num_workers": 1,

    "data_security_mode": "SINGLE_USER"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())