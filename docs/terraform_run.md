Terraform dry-run instructions

This repository includes a minimal Terraform skeleton at infra/terraform to provision an S3 bucket and an IAM user for MLflow artifacts.

DO NOT RUN APPLY UNLESS YOU KNOW THE COSTS.

1) Install Terraform (v1.5+ recommended).
2) cd infra/terraform
3) terraform init
4) terraform plan -var "bucket_name=your-unique-bucket-name"

The provided scripts/terraform_dryrun.ps1 runs init + plan for convenience.
Ensure AWS credentials are available in your environment before planning:
- set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY (or use aws configure)

Note: the Terraform is a skeleton; review and tighten IAM policies before applying in production.
