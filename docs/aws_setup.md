AWS (free-tier) setup recommendations

Goal: use AWS S3 for MLflow artifact storage while minimizing cost. Alternatives: use local MinIO to avoid AWS usage.

1) Minimal AWS S3 setup (free-tier eligible)
   - Create an S3 bucket (use the us-east-1 region to stay in free-tier).
   - Create an IAM user with programmatic access and policy limited to that bucket.
   - Store AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in environment variables or use AWS CLI credential store.

2) Configure MLflow to use S3
   - Set MLFLOW_S3_ENDPOINT_URL if using custom endpoint (not needed for AWS)
   - Set MLFLOW_TRACKING_URI to point to your MLflow server
   - Set AWS env vars: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
   - Example: export MLFLOW_TRACKING_URI=http://mlflow.example.com:5000
              export MLFLOW_S3_ENDPOINT_URL=https://s3.amazonaws.com
              export AWS_ACCESS_KEY_ID=...
              export AWS_SECRET_ACCESS_KEY=...

3) Use MinIO locally (recommended during development to avoid AWS charges)
   - docker-compose includes a MinIO service and MLflow configured to use it by default.
   - Start with: docker-compose up --build
   - Create bucket 'mlflow-artifacts' in MinIO console at http://localhost:9001

4) Upload artifacts to S3 (script provided)
   - python scripts/upload_to_s3.py --bucket your-bucket --prefix prophet

Notes
- Monitor S3 usage in the AWS Billing console. Keep lifecycle rules to delete old artifacts.
- For production on AWS, prefer EKS + managed RDS or DynamoDB for backend stores and S3 for artifacts.
