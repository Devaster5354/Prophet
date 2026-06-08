param(
    [string]$BucketName
)

if (-not (Get-Command terraform -ErrorAction SilentlyContinue)) {
    Write-Error 'Terraform not found in PATH. Install Terraform before running this script.'
    exit 2
}

if (-not $BucketName) {
    Write-Host 'Usage: .\scripts\terraform_dryrun.ps1 -BucketName <your-unique-bucket-name>'
    exit 1
}

Push-Location infra\terraform
try {
    terraform init
    terraform plan -var "bucket_name=$BucketName"
} finally {
    Pop-Location
}
