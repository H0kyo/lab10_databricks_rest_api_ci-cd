import os
import requests

url = "https://adb-7405605185991044.4.azuredatabricks.net/api/2.0/clusters/create"

token = os.getenv("PERSONAL_ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

data = {
    "cluster_name": "hrynchuk_lab10_cluster",
    "spark_version": "14.3.x-scala2.12",
    "node_type_id": "Standard_DS3_v2",
    "num_workers": 0,
    "azure_attributes": {
        "availability": "ON_DEMAND_AZURE"
    },
    "custom_tags": {
        "ResourceClass": "SingleNode"
    },
    "spark_conf": {
        "spark.databricks.cluster.profile": "singleNode"
    }
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())