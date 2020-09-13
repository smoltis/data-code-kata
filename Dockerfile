FROM python:3.7-slim
WORKDIR /parsers
COPY src/ ./
RUN pip install --no-cache-dir -r requirements.txt