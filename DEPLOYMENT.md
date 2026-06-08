## Deployment Guide

### Local Development
```bash
python -m venv .venv
. .\.venv\Scripts\activate  # Windows
pip install -r requirements-lock.txt
python scripts_setup_repo.py
docker-compose up --build
```

Then in separate terminals:
```bash
python models/train.py
python scripts_score_batch.py data/input.csv
```

Access:
- API: http://localhost:8000/health
- MLflow: http://localhost:5000
- MinIO: http://localhost:9001 (minioadmin/minioadmin)
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (admin/admin)

### AWS Deployment (Free-Tier)

1. **Provision S3 + IAM** (using Terraform):
```bash
cd infra/terraform
terraform plan -var "bucket_name=my-unique-bucket"
terraform apply  # only if you understand AWS charges
```

2. **Configure MLflow to use S3**:
```bash
export AWS_ACCESS_KEY_ID=<your_key>
export AWS_SECRET_ACCESS_KEY=<your_secret>
export MLFLOW_TRACKING_URI=http://<mlflow_host>:5000
```

3. **Upload artifacts**:
```bash
python scripts/upload_to_s3.py --bucket my-bucket --prefix prophet
```

4. **Deploy API** (ECS / EKS):
- Build image: `docker build -t prophet:latest .`
- Push to ECR: `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account>.dkr.ecr.us-east-1.amazonaws.com`
- Use k8s manifests in k8s/ for EKS or adapt for ECS

### Monitoring & Observability
- Prometheus scrapes /metrics from the API every 15 seconds
- Import Grafana dashboard: `python scripts/import_grafana.py` or manually upload dashboards/grafana_dashboard.json

### CI/CD
- Push to GitHub and CI workflow (.github/workflows/ci.yml) runs tests and builds Docker image
- Release workflow (.github/workflows/release.yml) can be triggered manually to create versioned releases

### Costs
- S3 storage: ~$0.023/GB/month (first 5GB free in 12-month free tier)
- ECS/EKS: check free-tier eligibility; t3.micro instances are typically within free tier
- Prometheus/Grafana: use Grafana Cloud free tier or host on free EC2 instance

For cost monitoring, set up AWS Budget alerts in the Billing dashboard.
