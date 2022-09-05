FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 80

CMD ["uvicorn", "user_api:app", "--reload", "--workers",  "1", "--host", "0.0.0.0", "--port", "80"]

