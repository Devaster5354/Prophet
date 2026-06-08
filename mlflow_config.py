import os
import mlflow


def get_tracking_uri():
    # Prefer environment override
    uri = os.environ.get('MLFLOW_TRACKING_URI')
    if uri:
        mlflow.set_tracking_uri(uri)
        return uri
    # Local mlruns folder
    path = os.path.abspath('mlruns')
    uri = f'file://{path}'
    mlflow.set_tracking_uri(uri)
    return uri


def init_experiment(name='prophet-experiment'):
    get_tracking_uri()
    if mlflow.get_experiment_by_name(name) is None:
        mlflow.create_experiment(name)
    mlflow.set_experiment(name)
    return name
