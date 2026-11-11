FROM python:3.11-slim

WORKDIR /app1
copy requirements.txt .
RUN pip intall --no-cache-dir -r requirements.txt
COPY . .
CMD ["python","app.py"]
