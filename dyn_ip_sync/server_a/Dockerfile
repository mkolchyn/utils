FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY .env .
COPY shared ./shared
COPY server_a ./server_a

# Expose port
EXPOSE 5000

# Run Flask server
CMD ["python", "-m", "server_a.server"]
