FROM python:3.14.0-slim
WORKDIR /backend
COPY . .
COPY requirement/base.txt .
COPY backend backend
RUN pip install --no-cache-dir -r requirement/base.txt
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
