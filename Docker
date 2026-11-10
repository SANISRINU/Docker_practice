FROM python:3.9 -slim
WROKDIR /APP
COPY requiremetns.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMP ["python', "app.py"]

