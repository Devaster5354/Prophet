"""Prefect flow to run training and batch scoring.
Requires prefect installed (added to requirements). This is a simple flow for demo/dev use.
"""
try:
    from prefect import flow, task
except Exception:
    # Prefect not installed; keep file import-safe
    flow = None
    def task(fn):
        return fn

from subprocess import run

@task
def run_training():
    # Run the training script
    res = run(['python', 'models/train.py'])
    return res.returncode

@task
def run_batch_scoring():
    # Example: score a sample CSV if present
    res = run(['python', 'scripts_score_batch.py', 'data/input.csv'])
    return res.returncode

if flow is not None:
    @flow(name='prophet-pipeline')
    def pipeline():
        r1 = run_training()
        r2 = run_batch_scoring()
        return (r1, r2)

    if __name__ == '__main__':
        pipeline()
else:
    if __name__ == '__main__':
        print('Prefect not installed. Run `pip install -r requirements-lock.txt` to enable flows.')
