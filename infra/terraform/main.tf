terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "mlflow_artifacts" {
  bucket = var.bucket_name
  acl    = "private"
}

resource "aws_iam_user" "mlflow_user" {
  name = "mlflow-user"
}

resource "aws_iam_user_policy" "mlflow_user_policy" {
  name = "mlflow-user-policy"
  user = aws_iam_user.mlflow_user.name
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = [
          "s3:PutObject",
          "s3:GetObject",
          "s3:ListBucket"
        ],
        Effect = "Allow",
        Resource = [
          "arn:aws:s3:::${var.bucket_name}",
          "arn:aws:s3:::${var.bucket_name}/*"
        ]
      }
    ]
  })
}
