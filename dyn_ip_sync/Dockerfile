FROM python:3.11-slim

WORKDIR /dynipsync

# Copy application code
COPY app ./app

# Install dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Run the app
CMD ["python", "app/main.py"]

