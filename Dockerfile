FROM python:3.10.4-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV ENV_FILE_PATH=.env

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
