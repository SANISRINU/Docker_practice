FROM python:3.11-slim

WORKDIR /app1

RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
COPY . .
CMD ["python","app.py"]
