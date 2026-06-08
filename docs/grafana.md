Grafana dashboard import

A sample Grafana dashboard JSON is included at dashboards/grafana_dashboard.json. To import:
1. Start Grafana (not included in docker-compose by default).
2. In Grafana UI, go to + -> Import
3. Upload dashboards/grafana_dashboard.json or paste its JSON
4. Select Prometheus as the data source and import.

Suggested panels
- Request rate (app_requests_total)
- Request latency (histogram_quantile over app_request_latency_seconds_bucket)
- Prediction distribution (from scores.csv via a simple datasource)

Tip: Grafana Cloud offers a free tier for small dashboards; export as JSON to keep in repo.
