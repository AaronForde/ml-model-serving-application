FROM python:3.9-slim

WORKDIR /app

COPY /serving/main.py /app/main.py

RUN pip install --no-cache-dir fastapi uvicorn[standard]

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]