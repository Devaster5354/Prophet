# Prepare release commit (PowerShell)
param(
    [string]$message = "chore: release - prepare repo for GitHub",
    [switch]$Push
)

Write-Host "Initializing git repo (if missing)"
if (-not (Test-Path .git)) {
    git init
}

git add .
git commit -m $message

Write-Host "Committed changes. To push to GitHub:
1. Create a remote repo on GitHub.
2. Run: git remote add origin https://github.com/<your-org>/<repo>.git
3. git branch -M main
4. git push -u origin main"

if ($Push) {
    git push -u origin main
}
