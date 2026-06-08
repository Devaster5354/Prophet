"""Import Grafana dashboard via API.
Usage: export GRAFANA_URL=http://localhost:3000
       export GRAFANA_API_KEY=<key>
       python scripts/import_grafana.py
"""
import os
import json
import requests

GRAFANA_URL = os.environ.get('GRAFANA_URL', 'http://localhost:3000')
API_KEY = os.environ.get('GRAFANA_API_KEY')
DASH_PATH = os.environ.get('GRAFANA_DASH_PATH', 'dashboards/grafana_dashboard.json')


def import_dashboard(grafana_url, api_key, dashboard_json_path):
    if api_key is None:
        raise SystemExit('GRAFANA_API_KEY env var required')
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    with open(dashboard_json_path, 'r') as f:
        payload = json.load(f)
    # payload may wrap dashboard in {"dashboard": {...}} already
    if 'dashboard' in payload:
        dashboard = payload['dashboard']
    else:
        dashboard = payload
    body = {"dashboard": dashboard, "overwrite": True}
    resp = requests.post(f"{grafana_url}/api/dashboards/db", headers=headers, json=body)
    resp.raise_for_status()
    return resp.json()


if __name__ == '__main__':
    res = import_dashboard(GRAFANA_URL, API_KEY, DASH_PATH)
    print('Imported dashboard:', res)
