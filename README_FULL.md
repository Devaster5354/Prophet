Prophet — Complete README (Deep)

1) Project purpose
Prophet is a reproducible marketing incrementality platform demonstrating CLV, uplift, churn, and purchase likelihood modeling. It includes a dev-friendly MLflow-backed training pipeline, a FastAPI scoring endpoint, Prefect flows for orchestration, local artifact storage via MinIO, Prometheus metrics, and infra guidance for AWS free-tier deployment.

2) Architecture
See diagrams/architecture.svg. Key components:
- Data ingestion & feature engineering (data/)
- Model training (models/train.py) with MLflow tracking
- Model registry (MLflow) and artifact store (MinIO or S3)
- Scoring API (api_app.py) for real-time predictions
- Batch scoring (scripts_score_batch.py)
- Monitoring: Prometheus + Grafana (dashboards/)
- Orchestration: Prefect flows (flows/prefect_flow.py)

3) Quick start (dev)
- python -m venv .venv && .\.venv\Scripts\activate
- pip install -r requirements-lock.txt
- python scripts_setup_repo.py
- docker-compose up --build
- python models/train.py
- python scripts_score_batch.py data/input.csv

4) Production (AWS, cost-conscious)
- Use S3 for artifacts; use Terraform skeleton (infra/terraform) to create a private bucket and restricted IAM user.
- For minimal cost, keep MLflow backend as sqlite and save artifacts to S3; use lifecycle rules to expire old artifacts (docs/s3_lifecycle.md).
- For deployment, build Docker image and deploy to EKS or ECS (skeleton k8s manifests in k8s/). Use AWS free-tier resources only for small testing.

5) Experiments & A/B
- API endpoint /experiment/assign records assignments to data/assignments.parquet.
- Use uplift modeling (causalml/econml) to compute ATT/ATE and calculate incremental CLV per user.
- ROI calculation helper: notebooks/roi_simulator.py and docs_ROI_calculation.md.

6) Observability & Monitoring
- /metrics endpoint exposes Prometheus metrics. Docker-compose includes Prometheus and Grafana (http://localhost:3000, default admin/admin).
- Import dashboards/grafana_dashboard.json manually or run scripts/import_grafana.py (requires GRAFANA_URL and GRAFANA_API_KEY). See docs/grafana_provisioning.md for programmatic import and provisioning guidance.
- Add alerting rules in production to notify on model drift and failed runs.

7) CI/CD & Tests
- CI workflow: .github/workflows/ci.yml runs lint + tests. Tests live in tests/.
- Use scripts/prepare_release.ps1 to prepare commits. Include Co-authored-by when committing via that script as needed.

8) Security & Cost notes
- Do not commit secrets. Use environment variables or AWS Secrets Manager.
- Limit S3 retention and enable lifecycle rules to avoid bills.

9) Resume & Business bullets
See RESUME_NOTES.md for finance-focused bullets, and docs/case_study.md for narrative to include in final README.

10) Next steps (todo)
- Enable MLflow server on an ECS Fargate task (cost varies).
- Replace MinIO with S3 for artifacts and enable registry via MLflow with S3 storage.
- Implement Grafana provisioning and dashboard automation.

Contact: Open an issue or edit RESUME_NOTES.md to refine metrics and narratives before pushing to GitHub.
