from fastapi.testclient import TestClient
from api_app import app

client = TestClient(app)


def test_metrics_endpoint():
    r = client.get('/metrics')
    assert r.status_code == 200
    assert 'app_requests_total' in r.text


def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json().get('status') == 'ok'
