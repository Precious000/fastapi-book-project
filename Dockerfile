FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "docker stop my-app || true && docker rm my-app || true && npm start"]


# Test Deployment Changes
# Test Deployment Changes
