FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements-lock.txt ./
RUN pip install --no-cache-dir -r requirements-lock.txt

# Copy project
COPY . .

EXPOSE 8000

CMD ["uvicorn","api_app:app","--host","0.0.0.0","--port","8000"]
