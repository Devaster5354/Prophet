Final pre-publish checklist

- [ ] Confirm RESUME_NOTES.md bullets are accurate and include metrics ($, %).
- [ ] Remove any PII from data/ and notebooks.
- [ ] Run pytest -q and ensure all tests pass.
- [ ] Run docker-compose up --build and verify /health and /metrics endpoints.
- [ ] Create GitHub repo and update remote URL in scripts/push_to_github.ps1 call.
- [ ] Run scripts/terraform_dryrun.ps1 if planning to provision S3 (dry-run only).
- [ ] Update docs/case_study.md with final numbers and narrative.
- [ ] Optional: replace MinIO settings with AWS credentials and run scripts/upload_to_s3.py to push artifacts.
