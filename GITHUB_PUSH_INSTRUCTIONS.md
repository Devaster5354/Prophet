# Push to GitHub - Instructions

## Prerequisites
1. Create a new repo on GitHub called "Prophet"
   - Go to https://github.com/new
   - Repo name: `Prophet`
   - Description: "Production-ready marketing incrementality platform with MLflow, FastAPI, and AWS integration"
   - Make it Public (for portfolio)
   - Do NOT initialize with README/license (we have our own)

2. Authenticate with GitHub
   - Option A: SSH setup (recommended)
     ```powershell
     # Generate SSH key (skip if you already have one)
     ssh-keygen -t ed25519 -C "your-email@example.com"
     # Add to GitHub: https://github.com/settings/ssh/new
     ```
   - Option B: Personal Access Token
     ```
     https://github.com/settings/tokens
     Create token with 'repo' scope
     ```

## Push Commands

### Using SSH (Recommended)
```powershell
git remote add origin git@github.com:YOUR_USERNAME/Prophet.git
git branch -M main
git push -u origin main
```

### Using HTTPS + PAT
```powershell
git remote add origin https://YOUR_USERNAME:YOUR_TOKEN@github.com/YOUR_USERNAME/Prophet.git
git branch -M main
git push -u origin main
```

### Using GitHub CLI (easiest)
```powershell
# Install: https://cli.github.com/
gh auth login
gh repo create Prophet --public --source=. --push --remote=origin
```

Replace:
- `YOUR_USERNAME` with your GitHub username (e.g., abhinivesh)
- `YOUR_TOKEN` with your Personal Access Token (if using HTTPS)

Run one of the above commands from the project root directory.
