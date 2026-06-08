Grafana provisioning (automated import)

This guide shows how to import dashboards programmatically into Grafana using the HTTP API.

1) Create an API key in Grafana (Organization -> API Keys) with Editor role.

2) Import via curl (example):

curl -X POST "http://<GRAFANA_HOST>:3000/api/dashboards/db" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <GRAFANA_API_KEY>" \
  -d '{ "dashboard": $(cat dashboards/grafana_dashboard.json), "overwrite": true }'

(When using Windows PowerShell, use Get-Content -Raw to embed JSON.)

3) Provisioning via files: place the JSON in /etc/grafana/provisioning/dashboards and add a datasource mapping in provisioning/datasources.

4) Importing programmatically (Python example):

import requests
import json

def import_dashboard(grafana_url, api_key, dashboard_json_path):
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    with open(dashboard_json_path, 'r') as f:
        dash = json.load(f)
    payload = {"dashboard": dash.get('dashboard', dash), "overwrite": True}
    r = requests.post(f"{grafana_url}/api/dashboards/db", headers=headers, json=payload)
    r.raise_for_status()
    return r.json()

5) Tips
- Use Grafana Cloud free tier for hosted dashboards.
- Keep dashboard JSON in repo for version control and reproducibility.
