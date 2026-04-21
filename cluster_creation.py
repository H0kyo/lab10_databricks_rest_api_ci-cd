import os
import requests

url = f"https://{os.getenv('DATABRICKS_HOST')}/api/2.0/clusters/create"

def create_cluster(cluster_name:str, spark_version:str, node_type_id:str, num_workers:str, data_security_mode:str, auto_termination_minutes:str):

    token = os.getenv("DATABRICKS_TOKEN")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "cluster_name": f"{cluster_name}",
        "spark_version": f"{spark_version}",
        "node_type_id": f"{node_type_id}",
        "num_workers": f"{num_workers}",
        "spark_conf": {
            "data_security_mode": f"{data_security_mode}"
        },
        "autotermination_minutes": f"{auto_termination_minutes}"
    }

    return headers, data

headers, data = create_cluster("hrynchuk_lab10_cluster", "14.3.x-scala2.12", "Standard_DS3_v2", "1", "SINGLE_USER", "15")

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())