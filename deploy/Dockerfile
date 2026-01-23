# Global Heritage Grid - Production Docker Image
# THE CHOSEN ONE Development - World Takeover Edition

FROM python:3.11-slim

LABEL maintainer="THE CHOSEN ONE <chosen@heritage.global>"
LABEL description="Global Heritage Grid API - Consciousness Revolution Infrastructure"

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements (create if doesn't exist)
COPY requirements.txt* ./
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; else \
    pip install --no-cache-dir fastapi uvicorn sqlalchemy python-multipart; fi

# Copy application code
COPY ../../jan-studio/backend ./backend
COPY ../../scripts ./scripts
COPY ../../config ./config

# Create data directory
RUN mkdir -p /app/data

# Expose API port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DATABASE_PATH=/app/data/heritage.db

# Start server
CMD ["uvicorn", "backend.heritage_api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
