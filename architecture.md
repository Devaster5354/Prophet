Architecture (ASCII)

[Data Sources] --> [Feature Engineering] --> [Model Training] --> [Model Registry / MLflow]
                                      |                         |
                                      v                         v
                                [Batch Scoring]           [FastAPI Scoring]
                                      |                         |
                                      v                         v
                                [Dashboards: Streamlit / Grafana] <-- [Monitoring]

Notes:
- Prefect orchestrates training + scoring flows.
- MLflow stores experiments; Models/model.pkl is a quick local artifact.
- Docker + docker-compose used for local deployment; use k8s for production.
