
FROM python:3.7.10-slim-buster

ENV PYTHONPATH="${PYTHONPATH}:/app"
WORKDIR "/app"

COPY requirements.txt .
COPY . .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir --progress-bar off -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8080
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]