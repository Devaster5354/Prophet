Prophet — Production scaffold

This repo contains a Streamlit marketing-impact demo and modeling artifacts. Files added by autopilot:
- Dockerfile, requirements-lock.txt, docker-compose.yml
- api_app.py (FastAPI scoring), scripts_score_batch.py
- Models/serialize.py helper
- ci.yml (copy to .github/workflows/ci.yml)
- scripts_setup_repo.py to create recommended directories

Next: run `python scripts_setup_repo.py`, then `docker-compose up --build` to start API.
