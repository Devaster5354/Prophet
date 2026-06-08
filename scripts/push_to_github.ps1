param(
    [string]$remoteUrl
)

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error 'git not found in PATH. Install git before running this script.'
    exit 2
}

if (-not $remoteUrl) {
    Write-Host 'Usage: .\scripts\push_to_github.ps1 -remoteUrl https://github.com/your/repo.git'
    exit 1
}

# Ensure clean working tree
$status = git status --porcelain
if ($status) {
    Write-Host 'Working tree has uncommitted changes. Commit or stash before pushing.'
    exit 1
}

git remote add origin $remoteUrl -f 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host 'Remote already exists. Updating origin URL.'
    git remote set-url origin $remoteUrl
}

git branch -M main

# Add Co-authored-by trailer to commit message if not present
$commit_msg = 'chore: release - prepare repo for GitHub`n`nCo-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>'

git commit --allow-empty -m $commit_msg

Write-Host 'Pushing to remote origin/main...'
git push -u origin main
