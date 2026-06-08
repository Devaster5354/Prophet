Prophet — Marketing Impact & Incrementality

Overview
A production-ready scaffold for marketing incrementality: CLV, uplift, churn models, MLflow tracking, Prefect flows, and a FastAPI scoring service. Designed for local dev with MinIO and for AWS deployment (free-tier friendly).

Quick start (dev)
1. python -m venv .venv && .\.venv\Scripts\activate
2. pip install -r requirements-lock.txt
3. python scripts_setup_repo.py
4. docker-compose up --build    # starts API, MLflow, MinIO, Prometheus
5. python models/train.py      # trains demo model and logs to MLflow
6. python scripts_score_batch.py data/input.csv

Testing & CI
- Local tests: pytest -q
- CI: .github/workflows/ci.yml runs lint + tests and can build Docker image.

AWS & Production notes
- Use docs/aws_setup.md for S3 + IAM guidance (free-tier eligible).
- Terraform skeleton present at infra/terraform for provisioning the S3 bucket and IAM user.
- For low-cost dev, keep using MinIO (docker-compose) and only push artifacts to S3 when needed.

Key endpoints
- GET /health — health check
- POST /predict — scoring (expects JSON {"features":[...]})
- POST /experiment/assign — record A/B assignment to data/assignments.parquet
- GET /metrics — Prometheus metrics

Runbook & maintenance
- Use scripts/check_mlflow.py to verify MLflow connectivity.
- Use scripts/upload_to_s3.py to push artifacts to S3 if needed.
- Use scripts/prepare_release.ps1 to prepare and commit a release-ready state.

Next automated steps
- Finalize Grafana dashboard import instructions (docs/grafana.md), Terraform dry-run script, and push-ready README with architecture diagram.

Contact
- For questions, edit RESUME_NOTES.md and docs/case_study.md to add business narratives and values.
