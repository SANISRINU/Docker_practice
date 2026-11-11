FROM python:3.11
WORKDIR /app1
COPY . /app1/
EXPOSE 500
CMD ["python","app.py"]
