S3 Lifecycle rule example to expire old MLflow artifacts

JSON example (apply via AWS Console or Terraform aws_s3_bucket_lifecycle_configuration):

{
  "Rules": [
    {
      "ID": "expire-old-artifacts",
      "Prefix": "mlruns/",
      "Status": "Enabled",
      "Expiration": { "Days": 90 }
    }
  ]
}

Recommendation: Keep last 90 days of artifacts; archive older artifacts to Glacier if needed to save cost.
