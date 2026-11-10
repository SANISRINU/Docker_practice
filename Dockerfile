FROM python:3.11 -slim
WORKDIR /app
COPY requiremetns.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python', "app.py"]

