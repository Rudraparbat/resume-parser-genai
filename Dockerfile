FROM python:3.13-slim

RUN apt-get update

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn" ,  "main:app" ,  "--workers 1" ,  "--worker-class", "uvicorn.workers.UvicornWorker" ,  "--bind" , "0.0.0.0:8000" , "--access-logfile" , "--log-level info"]

