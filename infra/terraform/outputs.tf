output "bucket_name" {
  value = aws_s3_bucket.mlflow_artifacts.bucket
}

output "mlflow_iam_user" {
  value = aws_iam_user.mlflow_user.name
}
