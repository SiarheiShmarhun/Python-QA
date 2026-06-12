# Dockerfile for a Flask application that displays a random cat GIF.
# This file automates the environment setup and application execution.

FROM python:3.9-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./
COPY templates/ ./templates/
EXPOSE 5001
CMD ["python", "app.py"]
