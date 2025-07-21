FROM python:3.9-slim

LABEL maintainer="automation@company.com"
LABEL description="Enterprise Invoice Processing Automation System"
LABEL version="1.0.0"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Create app user
RUN groupadd -r app && useradd -r -g app app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/
COPY config/ ./config/
COPY templates/ ./templates/
COPY .env.example .env

# Create necessary directories
RUN mkdir -p data logs && \
    chown -R app:app /app

# Switch to app user
USER app

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python src/main.py --health-check || exit 1

# Default command
CMD ["python", "src/main.py", "--help"]
