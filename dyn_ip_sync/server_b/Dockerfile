FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY .env .
COPY shared ./shared
COPY server_b ./server_b

# Run client
CMD ["python", "-m", "server_b.client"]
