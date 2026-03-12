FROM python:3.11-alpine

WORKDIR /app

# Alpine needs these for Pillow
RUN apk add --no-cache \
    gcc musl-dev \
    jpeg-dev zlib-dev libffi-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/
COPY frontend/ ./frontend/

EXPOSE 8080

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]