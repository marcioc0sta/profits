FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app

COPY . ./

RUN pip install --no-cache-dir -r requirements/prod.txt
