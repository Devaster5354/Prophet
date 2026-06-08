"""Check MLflow server connectivity by listing experiments."""
from mlflow_config import get_tracking_uri
import mlflow
import sys


def main():
    uri = get_tracking_uri()
    print('MLflow tracking URI:', uri)
    try:
        exps = mlflow.list_experiments()
        print(f'Found {len(exps)} experiments')
        print('MLflow OK')
    except Exception as e:
        print('MLflow connection failed:', e)
        sys.exit(2)

if __name__ == '__main__':
    main()
