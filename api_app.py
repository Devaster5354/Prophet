import time
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import typing as t
import os
import pandas as pd
from datetime import datetime
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI(title='Prophet Scoring API')

# Prometheus metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total HTTP requests', ['method','endpoint','http_status'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency seconds', ['endpoint'])

class PredictRequest(BaseModel):
    features: t.List[float]

class Assignment(BaseModel):
    user_id: str
    variant: str
    timestamp: t.Optional[str] = None

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/predict')
def predict(req: PredictRequest):
    model_path = os.path.join('Models', 'model.pkl')
    if os.path.exists(model_path):
        try:
            import joblib
            model = joblib.load(model_path)
            pred = model.predict([req.features])[0]
            return {'prediction': float(pred)}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    return {'prediction': 0.0, 'note': 'no serialized model found'}

@app.post('/experiment/assign')
def assign(a: Assignment):
    ts = a.timestamp or datetime.utcnow().isoformat()
    row = {'user_id': a.user_id, 'variant': a.variant, 'timestamp': ts}
    data_dir = os.path.join('data')
    os.makedirs(data_dir, exist_ok=True)
    out_path = os.path.join(data_dir, 'assignments.parquet')
    try:
        if os.path.exists(out_path):
            df = pd.read_parquet(out_path)
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        else:
            df = pd.DataFrame([row])
        df.to_parquet(out_path, index=False)
        return {'status': 'ok'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/metrics')
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        resp_time = time.time() - start
        try:
            endpoint = request.url.path
            REQUEST_LATENCY.labels(endpoint=endpoint).observe(resp_time)
            REQUEST_COUNT.labels(method=request.method, endpoint=endpoint, http_status=str(response.status_code)).inc()
        except Exception:
            pass
        return response

app.add_middleware(MetricsMiddleware)
