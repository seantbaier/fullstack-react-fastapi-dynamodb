FROM python:3.8

RUN mkdir -p /app
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]