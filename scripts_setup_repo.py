"""
Helper to create recommended directories and move scaffold files into place.
Run: python scripts_setup_repo.py
"""
import os
import shutil

ROOT = os.path.dirname(__file__)

def ensure(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Directories
dirs = [
    os.path.join(ROOT, '.github', 'workflows'),
    os.path.join(ROOT, 'tests'),
    os.path.join(ROOT, 'api'),
    os.path.join(ROOT, 'scripts'),
    os.path.join(ROOT, 'dashboards'),
    os.path.join(ROOT, 'docs'),
]
for d in dirs:
    ensure(d)

# Move ci.yml into .github/workflows if present
src_ci = os.path.join(ROOT, 'ci.yml')
if os.path.exists(src_ci):
    dst = os.path.join(ROOT, '.github', 'workflows', 'ci.yml')
    shutil.copy(src_ci, dst)
    print('Copied ci.yml to .github/workflows/ci.yml')

print('Repository scaffold directories created. Add or edit files in the new folders as needed.')
